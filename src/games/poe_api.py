import requests
import os

# TODO: Personal Preference, put it in a class instead of separate methods.
# TODO: Suggestion: Rename poe_api as it is VERY ismilar to poke_api. Maybe path_of_exile_api?
def poe_api(item_name: str, league: str = "Standard", amount_listing: int = 1):

    # TODO: Make it so only the proper leagues work. If I put in a league that doesn't exist, it shouldn't allow to make any request.

    # The data you want to send in your POST request
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

    # The headers you want to send with your POST request
    # TODO: Move headers to a spot where multiple functions can use it
    headers = {
        # TODO: Suggestion: Put the User-Agent in a separate env, so you can easily use it for all outgoing API requests
        'User-Agent': 'MehrainBot/0.0.1',
        'Cookie': os.getenv('POE_SESSION'),
    }

    # TODO: Put requests into two separate functions, have a "simple" main function that calls the two functions
    print("Sending POST request...")
    response = requests.post(f'https://www.pathofexile.com/api/trade/search/{league}', json=data, headers=headers)
    print("POST request completed!")

    # TODO: Handle non-successful (read, non-200) status codes properly in your requests. You can't assume that the request was successful and it shouldn't break your command call.
    response_data = response.json()

    print("Response data:")
    print(response_data)
    print(response_data.get('id'))
    print(response_data['result'][:amount_listing])

    request_id = response_data.get('id')
    cheapest_listings = response_data['result'][:amount_listing]
    listing_query = ','.join([listing for listing in cheapest_listings])

    trade_endpoint = f'https://www.pathofexile.com/api/trade/fetch/{listing_query}?query={request_id}'

    get_trades_response = requests.get(trade_endpoint, headers=headers)
    print(get_trades_response.status_code)
    print(get_trades_response.json())

    ###
    


poe_api("Tabula Rasa")

import base64

encoded_text = "SXRlbSBDbGFzczogQm9keSBBcm1vdXJzDQpSYXJpdHk6IFVuaXF1ZQ0KVGFidWxhIFJhc2ENClNpbXBsZSBSb2JlDQotLS0tLS0tLQ0KU29ja2V0czogVy1XLVctVy1XLVcgDQotLS0tLS0tLQ0KSXRlbSBMZXZlbDogODANCi0tLS0tLS0tDQpOb3RlOiB+cHJpY2UgMiBjaGFvcw0K=="
decoded_text = base64.b64decode(encoded_text).decode('utf-8')

print(decoded_text)