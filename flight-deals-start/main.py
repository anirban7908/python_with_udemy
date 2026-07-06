import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Conserve requests and preserve your free plan ====================
# Here we are not caching anything ending in *.sheety.co
# everything else is cached for 1 hour (3600 seconds). 
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# ==================== Talk to Sheety ====================
data_manager = DataManager()
sheety_data = data_manager.get_sheety_data()

# pprint(sheety_data[0])
# exit()

# ==================== Set the Dates ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))



# ==================== Search all the destinations ====================
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "CCU"

for destination in sheety_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        notify_manager = NotificationManager()
        pprint(f"Lower price flight found to {destination['city']}!")
        destination['origin_city_iata'] = ORIGIN_CITY_IATA
        # notify_manager.send_to_whatsapp(cheapest_flight, destination)
        notify_manager.send_to_phone(cheapest_flight, destination)
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.