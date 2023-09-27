import hypixel
import requests

import requests
import json

# Replace 'YOUR_API_KEY' with your actual Hypixel API key
API_KEY = '0d006f13-5bf1-48d1-8f5e-3211683278dc'

# Hypixel API base URL
BASE_URL = 'https://api.hypixel.net/'

# Function to fetch recently ended auctions
def get_recently_ended_auctions():
    try:
        print('starting')
        # Make a request to the Hypixel API to get the auction data
        response = requests.get(BASE_URL + 'skyblock/auctions', params={'key': API_KEY})
        response.raise_for_status()  # Raise an exception if the request fails
        data = response.json()
        print('x')

        # Check if the request was successful
        if data['success']:
            auctions = data['auctions']
            print('y')
            print(time.time())
            # Filter and print recently ended auctions
            for auction in auctions:
                print(auction['end'])
                if auction['end'] > int(time.time()):
                    print(f"Auction ID: {auction['uuid']}")
                    print(f"Item Name: {auction['item_name']}")
                    print(f"Starting Bid: {auction['starting_bid']} coins")
                    print(f"Bids: {auction['bids']}")
                    print("----")
        else:
            print("API request was not successful.")
            print(data['cause'])

    except Exception as e:
        print(f"An error occurred: {str(e)}")


import time
get_recently_ended_auctions()
