import requests


from dotenv import *
import os

load_dotenv(find_dotenv())

import requests


# Your Spree Sandbox API details
SPREE_API_URL = os.environ.get("SPREE_STORE_API_URL")
SPREE_API_KEY = os.environ.get("SPREE_STORE_API_KEY")


def get_products():
    response = requests.get(
        f"{SPREE_API_URL}/api/v3/store/products",
        headers={
            "x-spree-api-key": SPREE_API_KEY
        }
    )

    response.raise_for_status()

    data = response.json()['data']
    return data

def get_product(product_id:int):
    response = requests.get(
        f"{SPREE_API_URL}/api/v3/store/products/{product_id}",
        headers={
            "x-spree-api-key": SPREE_API_KEY
        }
    )

    response.raise_for_status()

    data = response.json()
    return data




if __name__ == "__main__":
    response = requests.get(
        f"{SPREE_API_URL}/api/v3/store/products",
        headers={
            "x-spree-api-key": SPREE_API_KEY
        }
    )

    response.raise_for_status()

    data = response.json()

    print(f"DATA: {data}")

    for product in data["data"]:
        print(product["name"], product["price"])