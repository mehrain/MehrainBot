import base64
import requests
import os

class PoETradeAPI:
    
    def __init__(self):
        self.base_url = "https://www.pathofexile.com/api/trade"
        self.headers = {
            'User-Agent': os.getenv('USER_AGENT'),
            'Cookie': os.getenv('POE_SESSION'),
        }

# TODO: Expand search filter to include more options
    def search_filter(self, item_name):
        data = {
            "query": {
                "status": {
                    "option": "online"
                },
                "name": item_name,
                "stats": [{
                    "type": "and",
                    "filters": []
                }]
            },
            "sort": {
                "price": "asc"
            }
        }
        
        return data   
    
    def parse_trade_response(self, search_response):
    
        for item in search_response['result']:	

            listing = item["listing"]
            
            item_price = listing["price"]
            item_whisper = listing["whisper"]

            price =  { 
                "amount": item_price["amount"],
                "currency": item_price["currency"]
                }

            print(price, item_whisper) 

    def search_item(self, item_name: str, league: str = "Standard", amount_listing: int = 1):
        # Send POST request to search for items
        print("Sending POST request...")
        search_body = self.search_filter(item_name)
        response = requests.post(f'{self.base_url}/search/{league}', json=search_body, headers=self.headers)        
        print("POST request completed!")

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Request failed with status code {response.status_code}")
            return

        # Get the response data
        response_data = response.json()

        # Print the response data
        # print("Response data:")
        # print(response_data)
        # print(response_data.get('id'))
        # print(response_data['result'][:amount_listing])

        # Get the request ID and the cheapest listings
        request_id = response_data.get('id')
        cheapest_listings = response_data['result'][:amount_listing]

        # Use the first listing as the ID for the fetch endpoint
        listing_id = ','.join(cheapest_listings)
        # print(listing_id)

        # Construct the trade URL
        trade_endpoint = f'{self.base_url}/fetch/{listing_id}?query={request_id}'
        # print(trade_endpoint)

        # Send GET request to fetch trade data
        get_trades_response = requests.get(trade_endpoint, headers=self.headers)
        # print(get_trades_response)
        # print(get_trades_response.status_code)
        # print(get_trades_response.json())

        trades = self.parse_trade_response(get_trades_response.json())
        
        return trades
        

PoETradeAPI().search_item(item_name="Headhunter", league="Standard", amount_listing=2)

