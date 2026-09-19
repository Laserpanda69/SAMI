import requests


from dotenv import *
import os

load_dotenv(find_dotenv())

import requests

# GET    /api/v3/products
# GET    /api/v3/products/:id
# GET    /api/v3/taxons
# GET    /api/v3/taxonomies
# POST   /api/v3/cart
# PATCH  /api/v3/cart/add_item
# PATCH  /api/v3/checkout
# GET    /api/v3/account

# GET    /api/v3/admin/orders
# POST   /api/v3/admin/products
# PATCH  /api/v3/admin/variants/:id
# DELETE /api/v3/admin/line_items/:id

# Your Spree Sandbox API details
SPREE_API_URL = os.environ.get("SPREE_STORE_API_URL")
SPREE_API_KEY = os.environ.get("SPREE_STORE_API_KEY")


def get_admin_token():
    NotImplemented()

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

def get_order(order_id:int):
    SPREE_STORE_ORDERS_API_KEY = os.environ.get("SPREE_STORE_ORDERS_API_KEY")
    response = requests.get(
        f"{SPREE_API_URL}/api/v3/admin/orders/{order_id}",
        headers={
            "x-spree-api-key": SPREE_STORE_ORDERS_API_KEY
        }
    )

    response.raise_for_status()

    data = response.json()
    return data

def get_orders(customer_id:str = None, customer_email:str = None):
    SPREE_STORE_ORDERS_API_KEY = os.environ.get("SPREE_STORE_ORDERS_API_KEY")
    response = requests.get(
        f"{SPREE_API_URL}/api/v3/admin/orders/",
        headers={
            "x-spree-api-key": SPREE_STORE_ORDERS_API_KEY
        },
        # params={
        #     "filter[customer_id]": customer_id 
        # }

    )

    response.raise_for_status()

    data = response.json()['data']
    if customer_id:
        data = [datum for datum in data if customer_id == datum['customer_id']]
    if customer_email:
        data = [datum for datum in data if customer_email == datum['email']]
    return data

def login(email:str, password:str):
    response = requests.post(
    f"{SPREE_API_URL}/api/v3/admin/auth/login",
    headers={
        "X-Spree-Api-Key": "sk_xxx",
        "Content-Type": "application/json"
    },
    json={
        "email": email,
        "password": password
        }
    )

    return response.json()


if __name__ == "__main__":
    None