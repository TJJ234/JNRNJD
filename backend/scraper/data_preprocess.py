from llama_index.llms.openai import OpenAI
import json
from .models import Car
from .data_download import WriteAuctionToSiteCSV
import asyncio

MANUFACTURER_COLUMN = "Company"
MODEL_COLUMN = "Model"

def IsCarValid(car: Car):
    return not (
        car.brand is None or
        car.model is None or
        car.year is None or
        car.price is None or
        car.image_link is None or
        car.link is None
    )

llm = OpenAI(model="gpt-4o-mini", temperature=0)

# The difference between langchain_openai ChatOpenAI and llamaindex OpenAI is negligible
# Allow multiple llm.acompletes to run so we don't wait for each one
LLMCarRequests = []
LLMCarAsyncRequestLimit = 20
async def StoreLLMCarRequest(query: str, additional_values: dict):
    LLMCarRequests.append({"query": query, "additional_values": additional_values})

    if len(LLMCarRequests) == LLMCarAsyncRequestLimit:
        tasks = []
        for request in LLMCarRequests:
            tasks.append(llm.acomplete(request["query"]))
        results = await asyncio.gather(*tasks)

        for i in range(0, len(results) - 1):
            result = results[i].text
            additional = LLMCarRequests[i]["additional_values"]

            obj = None
            try:
                obj = json.loads(result)
                obj["year"] = ParseYear(obj["year"])
                obj["price"] = ParseCarPrice(obj["price"])
                website = additional["website"]
                additional.pop("website")
                obj = obj | additional
                if website:
                    WriteAuctionToSiteCSV(website, obj)
            except Exception as e:
                print("Error decoding JSON:", e)

async def ExtractAndStoreCarInfo(text: str, additional_values: dict):
    await StoreLLMCarRequest(f"""
        Extract structured data from the following text and return it as a JSON object with no extra characters or formatting.
        If you can't find certain data keep the value as null.

        Text: {text}
            
        Format:
        {{
            "brand": "Brand",
            "model": "Model",
            "year": "Year",
            "price": "The price followed by the currency symbol seperated by an empty space, if the car is sold by agreement or this is null set this to \"0 €\"",
            "by_agreement": "if the car is sold by agreement set this to true",
            "mileage_km": "Kilometers driven",
            "transmission": "Transmission type",
            "fuel_type": "Fuel type",
            "color": "Color",
            "registration": "Registration",
            "registration_date": "Registration Date",
            "damaged": "Analyse the text and set this to true or false if the car is damaged or is for parts. If this is null set it to false.",
        }}
    """, additional_values)

def ParseCarPrice(price: str) -> int:
    split = price.split(" ")
    number = split[0]
    currency = split[1]
    number = number.replace(".", "")

    if currency.lower() in ["€", "еур", "eur", "euro"]:
        return int(number)
    elif currency.lower() in ["ден", "mkd", "den", "мкд"]:
        return int(number) / 60
    elif currency.lower() in ["$", "usd"]:
        return int(number) * 0.92
    else:
        raise Exception("Error parsing the price!")

def ParseYear(year: str) -> int:
    try: 
        return (0 if year.lower() == "none" else int(year))
    except Exception as e:
        print("Error parsing the year ", e)