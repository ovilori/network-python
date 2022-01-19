'''1. This program uses regular expression to extract the IP addresses from the output of a traceroute command saved to a txt file
       see .
    2. Uses the Netaddr library to verify if the IP address is a public IPV4 address.
    3. Makes a GET request to https://api.ipgeolocation.io/ipgeo to obtain the geolocation information of each ipv4 address.
    4. Save each response to a JSON file and then an excel spreadsheet.

    shout-out to https://github.com/network-charles/Traceroute-Data-to-IP-Geolocation-Data.
'''
import requests #HTTP request library to make API requests
from netaddr import * #module for working with IP address
import re  #regular expression (regex) module to manipulate strings
import pandas as pd

#declaring an empty list to store public IPV4 addresses
public_ipv4_addresses  = []

#opening the output of the traceroute saved to Google.txt
with open('Google.txt', 'r') as file:
    for line in file:
        #shoutout to https://feralpacket.org/?p=817 for the IPV4 regex below
        ipv4_regex = re.compile(r'''(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}
                        (?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])''', re.VERBOSE)

        #searching for IPV4 address in the traceroute result
        ipv4_address = ipv4_regex.search(line)

        #defining a condition to save found IPV4 address to a variable
        if ipv4_address:
            ipv4_address = ipv4_address.group(0)
 
            #converting the string IPV4 address found to actual IPV4 address using the Netaddr library
            ipv4_address = IPAddress(ipv4_address)
            
            #verify if the IP address is a public IP address and append to the public IPV4 list
            if ipv4_address.is_unicast() and not ipv4_address.is_private():
                public_ipv4_addresses.append(ipv4_address)
            else:
                continue
    
    for idx, ipv4_address in enumerate(public_ipv4_addresses):
        #coverting the public IPV4 address back to string format
        ipv4_address = str(ipv4_address)

        #making an API call to https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=1.1.1.1&fields=geo to obtain geolocation information only.
        ip_geolocation_info = requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=your_api_key&ip=%s&fields=geo' %(ipv4_address))
        
        #storing the API response as text
        geo_information = ip_geolocation_info.text

        #creating a file to save the text response of each API call to a JSON file. The 'a' options appends the response to the end of the file.
        json_doc = open('geo_information.json', 'a')

        #writing the response for each API call to the JSON file on a new line
        json_doc.write(f'{geo_information}\n')

        #closing the file
        json_doc.close()

#using Pandas to read the JSON file
json_doc_to_excel = pd.read_json('geo_information.json', lines=True)

#saving to excel sheet.
json_doc_to_excel.to_excel('ip_geo_info.xlsx', sheet_name='ip_geoinformation', index=False)
