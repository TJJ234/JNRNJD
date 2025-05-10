from django.db import models
from dataclasses import dataclass

WEBSITES = {
    "reklama5": {"domain": "reklama5.mk", "listings": "https://reklama5.mk/Search?city=&cat=24&q=&sell=0&sell=1&buy=0&buy=1&trade=0&trade=1&includeOld=0&includeOld=1&includeNew=0&includeNew=1&cargoReady=0&DDVIncluded=0&private=0&company=0&SortByPrice=0&zz=1&pageView=&page=1"},
    "pazar3": {"domain": "pazar3.mk", "listings": "https://www.pazar3.mk/oglasi/vozila/avtomobili/prodazba?Page=1"},
    "autowelt": {"domain": "autowelt.mk", "listings": "https://autowelt.mk/vehicles"},
    "toyota": {"domain": "toyota.com.mk", "listings": "https://www.toyota.com.mk/vozila/koristeni/"},
    "vozi": {"domain": "vozi.com", "listings": "https://vozi.com/mk/prebaruvaj/avtomobili/makedonija?page=1"},
}

@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: int
    by_agreement: bool
    mileage_km: int
    transmission: str
    fuel_type: str
    color: str
    registration: str
    registration_date: str
    damaged: bool
    image_link: str
    link: str

# Create your models here.