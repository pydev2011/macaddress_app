from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

search = input("Enter the search param (IP address e.g. '44:38:39:ff:ef:57'): ")
URL = "https://api.macaddress.io/v1?"
PARAMS = {"apiKey": "at_Km5ZQXTnfRsg42KBdeafhBpCdRuUP",
          "output": "json",
          "search": search}

url = URL + '&'.join([k + '=' + v for k, v in PARAMS.items()])

req = Request(url)
try:
    response = urlopen(req)
except HTTPError as e:
    print("The server couldn't fulfill the request.")
    print('Error code: ', e.code)
    print('Error: ', e.read())
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    response = json.loads(response.read())
    company_name = response['vendorDetails']['companyName']
    company_address = response['vendorDetails']['companyAddress']
    print("Company Name: ", '\033[94m' + company_name + '\033[0m')
    print("Company Address: ", '\033[94m' + company_address + '\033[0m')
