import requests
# Need to import key from secrets_1
from secrets_1 import key

response = requests.get('http://www.mapquestapi.com/geocoding/v1/address',
                        params={'key': key, 'location': 'Boston, MA'})
