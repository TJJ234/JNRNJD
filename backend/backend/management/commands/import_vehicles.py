import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from pathlib import Path

class Command(BaseCommand):
    help = 'Imports vehicle data directly from CSV to PostgreSQL'

    def handle(self, *args, **options):
        csv_path = Path(settings.BASE_DIR) / 'data' / 'import' / 'koli.csv'
        
        self.stdout.write(f"Attempting to import from: {csv_path}")
        
        if not csv_path.exists():
            self.stderr.write(self.style.ERROR(f"CSV file not found at {csv_path}"))
            return

        try:
            with connection.cursor() as cursor:
                # Create table matching Django's expected format
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS scraper_vehicle (
                    id SERIAL PRIMARY KEY,
                    brand VARCHAR(100),
                    model VARCHAR(100),
                    year INTEGER,
                    price DECIMAL(12,2),
                    by_agreement BOOLEAN DEFAULT FALSE,
                    mileage_km VARCHAR(50),
                    transmission VARCHAR(50),
                    fuel_type VARCHAR(50),
                    color VARCHAR(50),
                    registration VARCHAR(50),
                    registration_date VARCHAR(50),
                    damaged BOOLEAN DEFAULT FALSE,
                    image_link TEXT,
                    link TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                )
                """)
                
                # Clear existing data
                cursor.execute("TRUNCATE TABLE scraper_vehicle RESTART IDENTITY")
                
                # Import data
                with open(csv_path, encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for i, row in enumerate(reader, 1):
                        cursor.execute("""
                        INSERT INTO scraper_vehicle (
                            brand, model, year, price, by_agreement, mileage_km,
                            transmission, fuel_type, color, registration,
                            registration_date, damaged, image_link, link
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s,
                            %s, %s, %s, %s
                        )
                        """, [
                            row['brand'],
                            row['model'],
                            int(float(row['year'])) if row['year'] else None,
                            float(row['price']) if row['price'] else None,
                            row['by_agreement'].lower() == 'true',
                            row['mileage_km'],
                            row['transmission'],
                            row['fuel_type'],
                            row['color'],
                            row['registration'],
                            row['registration_date'] or None,
                            row['damaged'].lower() == 'true',
                            row['image_link'],
                            row['link']
                        ])
                        if i % 100 == 0:
                            self.stdout.write(f"Processed {i} records...")
                
                self.stdout.write(self.style.SUCCESS(
                    f"Successfully imported {i} vehicles from {csv_path}"
                ))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error on row {i+1}: {str(e)}"))
            raise