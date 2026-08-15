import requests
import time

def get_region_all_orders_by_item_type(item):
    BASE_URL_API = "https://evetycoon.com/api/v1/market/orders/"
    url = f"{BASE_URL_API}{item}"
    return requests.get(url)


paused = False
item = input("Enter Item Id: ")
while True and not paused:
    print("Getting item market data...")
    response = get_region_all_orders_by_item_type(item)
    if response.ok:
        print(response.json())
        time.sleep(300)