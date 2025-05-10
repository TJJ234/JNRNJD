
from langchain_neo4j import Neo4jGraph
import pandas as pd
from typing import List
from .models import Car
import os

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="neo4j",
)

graph.query("MATCH(n) DETACH DELETE n")

csvs = os.listdir("scraper/data")
for csv in csvs:
    data = pd.read_csv("scraper/data/" + csv)
    for index, row in data.iterrows():
        properties = ', '.join([f"{key}: '{value}'" if isinstance(value, str) else f"{key}: {value}" 
                                for key, value in row.to_dict().items()])

        query = f"""
            CREATE (c:Car {{ {properties} }})
        """
        graph.query(query)

graph.query("""
    MATCH (a:Car), (b:Car)
    WHERE a.brand = b.brand AND a.link <> b.link
    CREATE (a)-[:SAME_BRAND]->(b)
""")

graph.query("""
    MATCH (a:Car), (b:Car)
    WHERE a.model = b.model AND a.link <> b.link
    CREATE (a)-[:SAME_MODEL]->(b)
""")

graph.query("""
    MATCH (a:Car), (b:Car)
    WHERE a.year = b.year AND a.link <> b.link
    CREATE (a)-[:SAME_YEAR]->(b)
""")

properties = ['brand', 'model', 'year', 'price', 'transmission', 'fuel_type', 'color', 'registration']
for prop in properties:
    graph.query(f"CREATE INDEX FOR (n:Car) ON (n.{prop});")

class Filter:
    brand: str
    model: str
    year_min: int
    year_max: int
    price_min: int
    price_max: int
    by_agreement: bool
    mileage_km_min: int
    mileage_km_max: int
    transmission: str
    fuel_type: str
    color: str
    registration: str
    registration_date_min: str
    registration_date_max: str
    damaged: bool

def MatchByFilter(filter: Filter) -> List[Car]:
    print("test")
    
#graph.query("""
#MATCH (a:Car), (b:Car)
#WHERE ABS(a.price - b.price) < 10000 AND a.id <> b.id
#CREATE (a)-[:SIMILAR_PRICE]->(b)
#""")