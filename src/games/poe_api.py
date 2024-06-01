import base64
import requests
import os


# TODO: Suggestion: Rename poe_api as it is VERY ismilar to poke_api. Maybe path_of_exile_api?

class PoETradeAPI:
    
    def __init__(self):
        self.base_url = "https://www.pathofexile.com/api/trade"
        self.headers = {
            'User-Agent': os.getenv('USER_AGENT'),
            'Cookie': os.getenv('POE_SESSION'),
        }
        self.data = {}


# TODO: 
    def search_filter(self, item_name):
        self.data = {
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

    def search_item(self, item_name: str, league: str = "Standard", amount_listing: int = 1):
        # Send POST request to search for items
        print("Sending POST request...")
        self.search_filter(item_name)
        response = requests.post(f'{self.base_url}/search/{league}', json=self.data, headers=self.headers)        
        print("POST request completed!")

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Request failed with status code {response.status_code}")
            return

        # Get the response data
        response_data = response.json()

        # Print the response data
        print("Response data:")
        print(response_data)
        print(response_data.get('id'))
        print(response_data['result'][:amount_listing])

        # Get the request ID and the cheapest listings
        request_id = response_data.get('id')
        cheapest_listings = response_data['result'][:amount_listing]

        # Use the first listing as the ID for the fetch endpoint
        listing_id = cheapest_listings[0]

        # Construct the trade endpoint URL
        trade_endpoint = f'{self.base_url}/fetch/{listing_id}?query={request_id}'
        print(trade_endpoint)

        # Send GET request to fetch trade data
        get_trades_response = requests.get(trade_endpoint, headers=self.headers)
        print(get_trades_response)
        print(get_trades_response.status_code)
        print(get_trades_response.json())

        ###
        

PoETradeAPI().search_item(item_name="Blackflame", league="Standard", amount_listing=1)

# import base64

# encoded_text = "SXRlbSBDbGFzczogQm9keSBBcm1vdXJzDQpSYXJpdHk6IFVuaXF1ZQ0KVGFidWxhIFJhc2ENClNpbXBsZSBSb2JlDQotLS0tLS0tLQ0KU29ja2V0czogVy1XLVctVy1XLVcgDQotLS0tLS0tLQ0KSXRlbSBMZXZlbDogODANCi0tLS0tLS0tDQpOb3RlOiB+cHJpY2UgMiBjaGFvcw0K=="
# decoded_text = base64.b64decode(encoded_text).decode('utf-8')

# print(decoded_text)

# {', 'realm': 'pc'}, 'price': {'type': '~price', 'amount': 100, 'currency': 'chaos'}}, 'item': {'verified': True, 'w': 1, 'h': 1, 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvUmluZ3MvQmxhY2tGbGFtZUZpcmUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/d8cb90fe20/BlackFlameFire.png', 'league': 'Standard', 'id': '57ff0b352f0253a5a56b14cb5164bb518aa185e8f6e2864890fc77fd55d6f88a', 'name': 'Blackflame', 'typeLine': 'Amethyst Ring', 'baseType': 'Amethyst Ring', 'rarity': 'Unique', 'ilvl': 81, 'identified': True, 'note': '~price 100 chaos', 'corrupted': True, 'requirements': [{'name': 'Level', 'values': [['49', 0]], 'displayMode': 0, 'type': 62}], 'implicitMods': ['+21% to Chaos Resistance'], 'explicitMods': ['+8% to Fire Damage over Time Multiplier', '50% reduced Ignite Duration on Enemies', '15% chance to Ignite', 'Enemies Ignited by you take Chaos Damage instead of Fire Damage from Ignite', 'Withered does not expire on Enemies Ignited by you', '+25% to Fire and Chaos Resistances'],
#     'result': [ 'flavourText': ['Beyond the veil of death, there burns a fire\r', 'by whose light night is borne.'], 'frameType': 3, 'extended': {'mods': {'explicit': [{'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_3382807662', 'min': 8, 'max': 12}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_1086147743', 'min': -50, 'max': -50}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_1335054179', 'min': 10, 'max': 15}]}, {'name': '', 'tier': '', 'level': 62, 'magnitudes': [{'hash': 'explicit.stat_2714810050', 'min': 1, 'max': 1}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_279110104', 'min': 1, 'max': 1}]}, {'name': '', 'tier': '', 'level': 1, 'magnitudes': [{'hash': 'explicit.stat_378817135', 'min': 20, 'max': 25}]}], 'implicit': [{'name': '', 'tier': '', 'level': 38, 'magnitudes': [{'hash': 'implicit.stat_2923486259', 'min': 17, 'max': 23}]}]}, 'hashes': {'explicit'
#         {: [['explicit.stat_3382807662', [0]], ['explicit.stat_1086147743', [1]], ['explicit.stat_1335054179', [2]], ['explicit.stat_2714810050', [3]], ['explicit.stat_279110104', [4]], ['explicit.stat_378817135', [5]]], 'implicit': [['implicit.stat_2923486259', [0]]]}, 'text': 'SXRlbSBDbGFzczogUmluZ3MNClJhcml0eTogVW5pcXVlDQpCbGFja2ZsYW1lDQpBbWV0aHlzdCBSaW5nDQotLS0tLS0tLQ0KUmVxdWlyZW1lbnRzOg0KTGV2ZWw6IDQ5DQotLS0tLS0tLQ0KSXRlbSBMZXZlbDogODENCi0tLS0tLS0tDQorMjElIHRvIENoYW9zIFJlc2lzdGFuY2UgKGltcGxpY2l0KQ0KLS0tLS0tLS0NCis4JSB0byBGaXJlIERhbWFnZSBvdmVyIFRpbWUgTXVsdGlwbGllcg0KNTAlIHJlZHVjZWQgSWduaXRlIER1cmF0aW9uIG9uIEVuZW1pZXMNCjE1JSBjaGFuY2UgdG8gSWduaXRlDQpFbmVtaWVzIElnbml0ZWQgYnkgeW91IHRha2UgQ2hhb3MgRGFtYWdlIGluc3RlYWQgb2YgRmlyZSBEYW1hZ2UgZnJvbSBJZ25pdGUNCldpdGhlcmVkIGRvZXMgbm90IGV4cGlyZSBvbiBFbmVtaWVzIElnbml0ZWQgYnkgeW91DQorMjUlIHRvIEZpcmUgYW5kIENoYW9zIFJlc2lzdGFuY2VzDQotLS0tLS0tLQ0KQmV5b25kIHRoZSB2ZWlsIG9mIGRlYXRoLCB0aGVyZSBidXJucyBhIGZpcmUNCmJ5IHdob3NlIGxpZ2h0IG5pZ2h0IGlzIGJvcm5lLg0KLS0t
#             'id': '57ff0b352f0253a5a56b14cb5164bb518aa185e8f6e2864890fc77fd55d6f88a',LS0tLS0NCkNvcnJ1cHRlZA0KLS0tLS0tLS0NCk5vdGU6IH5wcmljZSAxMDAgY2hhb3MNCg=='}}}]}
#             'listing': {
#                 'method': 'psapi',
#                 'indexed': '2024-06-01T06:23:24Z',
#                 'stash': {
#                     'name': 'Shop1',
#                     'x': 0,
#                     'y': 1
#                 },
#                 'whisper': '@Эляпь Здравствуйте, хочу купить у вас Чёрное пламя Кольцо с аметистом за 100 chaos в лиге Standard (секция "Shop1"; позиция: 1 столбец, 2 ряд)',
#                 'whisper_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMWVlMWQ2NWRlNDAwODhiMGNjZjljZTU2ZWMxMmQwMCIsImlzcyI6ImFyM1k3UjdmZSIsImF1ZCI6ImQwOTQ3N2YxLWNhMWUtNGJlMC1iOTYyLTg5NDUyZDc3YTk0YSIsImRzdCI6Ilx1MDQyZFx1MDQzYlx1MDQ0Zlx1MDQzZlx1MDQ0YyIsImxvYyI6InJ1X1JVIiwidG9rIjoiaXRlbSIsInN1YiI6IjU3ZmYwYjM1MmYwMjUzYTVhNTZiMTRjYjUxNjRiYjUxOGFhMTg1ZThmNmUyODY0ODkwZmM3N2ZkNTVkNmY4OGEiLCJkYXQiOiI4ZDE5YzBkMDJkN2I3ZWI4ZTkzMzUzMDIyNDg0MjdjZSIsImlhdCI6MTcxNzI1MjU2NCwiZXhwIjoxNzE3MjUyODY0fQ.us8TC9lXXLypWGQKqJObmOyyUSDKPODLzowIurQr770',
#                 'account': {
#                     'name': 'sunny_guest',
#                     'online': {
#                         'league': 'Standard'
#                     },
#                     'lastCharacterName': 'Эляпь',
#                     'language': 'ru_RU',
#                     'realm': 'pc'
#                 },
#                 'price': {
#                     'type': '~price',
#                     'amount': 100,
#                     'currency': 'chaos'
#                 }
#             },
#             'item': {
#                 'verified': True,
#                 'w': 1,
#                 'h': 1,
#                 'icon': 'https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvUmluZ3MvQmxhY2tGbGFtZUZpcmUiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/d8cb90fe20/BlackFlameFire.png',
#                 'league': 'Standard',
#                 'id': '57ff0b352f0253a5a56b14cb5164bb518aa185e8f6e2864890fc77fd55d6f88a',
#                 'name': 'Blackflame',
#                 'typeLine': 'Amethyst Ring',
#                 'baseType': 'Amethyst Ring',
#                 'rarity': 'Unique',
#                 'ilvl': 81,
#                 'identified': True,
#                 'note': '~price 100 chaos',
#                 'corrupted': True,
#                 'requirements': [
#                     {
#                         'name': 'Level',
#                         'values': [
#                             ['49', 0]
#                         ],
#                         'displayMode': 0,
#                         'type': 62
#                     }
#                 ],
#                 'implicitMods': ['+21% to Chaos Resistance'],
#                 'explicitMods': [
#                     '+8% to Fire Damage over Time Multiplier',
#                     '50% reduced Ignite Duration on Enemies',
#                     '15% chance to Ignite',
#                     'Enemies Ignited by you take Chaos Damage instead of Fire Damage from Ignite',
#                     'Withered does not expire on Enemies Ignited by you',
#                     '+25% to Fire and Chaos Resistances'
#                 ],
#                 'flavourText': [
#                     'Beyond the veil of death, there burns a fire\r',
#                     'by whose light night is borne.'
#                 ],
#                 'frameType': 3,
#                 'extended': {
#                     'mods': {
#                         'explicit': [
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 1,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_3382807662',
#                                         'min': 8,
#                                         'max': 12
#                                     }
#                                 ]
#                             },
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 1,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_1086147743',
#                                         'min': -50,
#                                         'max': -50
#                                     }
#                                 ]
#                             },
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 1,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_1335054179',
#                                         'min': 10,
#                                         'max': 15
#                                     }
#                                 ]
#                             },
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 62,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_2714810050',
#                                         'min': 1,
#                                         'max': 1
#                                     }
#                                 ]
#                             },
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 1,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_279110104',
#                                         'min': 1,
#                                         'max': 1
#                                     }
#                                 ]
#                             },
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 1,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'explicit.stat_378817135',
#                                         'min': 20,
#                                         'max': 25
#                                     }
#                                 ]
#                             }
#                         ],
#                         'implicit': [
#                             {
#                                 'name': '',
#                                 'tier': '',
#                                 'level': 38,
#                                 'magnitudes': [
#                                     {
#                                         'hash': 'implicit.stat_2923486259',
#                                         'min': 17,
#                                         'max': 23
#                                     }
#                                 ]
#                             }
#                         ]
#                     },
#                     'hashes': {
#                         'explicit': [
#                             [
#                                 'explicit.stat_3382807662',
#                                 [0]
#                             ],
#                             [
#                                 'explicit.stat_1086147743',
#                                 [1]
#                             ],
#                             [
#                                 'explicit.stat_1335054179',
#                                 [2]
#                             ],
#                             [
#                                 'explicit.stat_2714810050',
#                                 [3]
#                             ],
#                             [
#                                 'explicit.stat_279110104',
#                                 [4]
#                             ],
#                             [
#                                 'explicit.stat_378817135',
#                                 [5]
#                             ]
#                         ],
#                         'implicit': [
#                             [
#                                 'implicit.stat_2923486259',
#                                 [0]
#                             ]
#                         ]
#                     },
#                     'text': 'SXRlbSBDbGFzczogUmluZ3MNClJhcml0eTogVW5pcXVlDQpCbGFja2ZsYW1lDQpBbWV0aHlzdCBSaW5nDQotLS0tLS0tLQ0KUmVxdWlyZW1lbnRzOg0KTGV2ZWw6IDQ5DQotLS0tLS0tLQ0KSXRlbSBMZXZlbDogODENCi0tLS0tLS0tDQorMjElIHRvIENoYW9zIFJlc2lzdGFuY2UgKGltcGxpY2l0KQ0KLS0tLS0tLS0NCis4JSB0byBGaXJlIERhbWFnZSBvdmVyIFRpbWUgTXVsdGlwbGllcg0KNTAlIHJlZHVjZWQgSWduaXRlIER1cmF0aW9uIG9uIEVuZW1pZXMNCjE1JSBjaGFuY2UgdG8gSWduaXRlDQpFbmVtaWVzIElnbml0ZWQgYnkgeW91IHRha2UgQ2hhb3MgRGFtYWdlIGluc3RlYWQgb2YgRmlyZSBEYW1hZ2UgZnJvbSBJZ25pdGUNCldpdGhlcmVkIGRvZXMgbm90IGV4cGlyZSBvbiBFbmVtaWVzIElnbml0ZWQgYnkgeW91DQorMjUlIHRvIEZpcmUgYW5kIENoYW9zIFJlc2lzdGFuY2VzDQotLS0tLS0tLQ0KQmV5b25kIHRoZSB2ZWlsIG9mIGRlYXRoLCB0aGVyZSBidXJucyBhIGZpcmUNCmJ5IHdob3NlIGxpZ2h0IG5pZ2h0IGlzIGJvcm5lLg0KLS0tLS0tLS0NCkNvcnJ1cHRlZA0KLS0tLS0tLS0NCk5vdGU6IH5wcmljZSAxMDAgY2hhb3MNCg=='
#                 }
#             }
#         }
#     ]
# }

