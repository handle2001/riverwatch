# Riverwatch
# Periodically fetch river gauge metrics from USGS
import json
import requests
import time

API_URL = "https://waterservices.usgs.gov/nwis/iv/"
API_RESPONSE_FORMAT = "json"

# Get list of site codes to query for
# For now just use "03451500" French Broad at Asheville
# TODO: Put the list of sites in a file or DB table

sites = ["03451500"]
site_data  = {}

# Pull data from USGS for all sites[]
for site in sites:
    payload = {'format':API_RESPONSE_FORMAT,'sites':site}

    try:
        r = requests.get(API_URL, params=payload)

    except:
        print(f"There was an error fetching site ${site} from ${API_URL}")
        print(r.status_code)

    raw_data = json.loads(r.text)
    raw_data = raw_data['value']['timeSeries']
    site_data[site] = {
        'siteName': raw_data[0]['sourceInfo']['siteName'],
        #'timeStamp': raw_data[0]['values'][0]['value'][0]['dateTime'],
        'temperature': raw_data[0]['values'][0]['value'][0]['value'],
        'precipitation': raw_data[1]['values'][0]['value'][0]['value'],
        'discharge': raw_data[2]['values'][0]['value'][0]['value'],
        'height': raw_data[3]['values'][0]['value'][0]['value'],
        'conductance': raw_data[4]['values'][0]['value'][0]['value'],
        'dissolved_oxygen': raw_data[5]['values'][0]['value'][0]['value'],
        'pH': raw_data[6]['values'][0]['value'][0]['value'],
        'height_above_datum': raw_data[7]['values'][0]['value'][0]['value'],
        'turbidity': raw_data[8]['values'][0]['value'][0]['value'],
    }

# timeSeries
# 0 = temperature in degrees C
# 1 = precipitation total in inches
# 2 = discharge in cubic ft/s
# 3 = gauge height in feet
# 4 = specific conductance in microsiemens
# 5 = dissolved oxygen in mg/L
# 6 = pH in standard units
# 7 = stream water level in ft above NAVD 1988
# 8 = turbidity in formazin nephelometric units
# Actual value is under value[timeSeries][<index (from above)>][values][value][0][value]
# Timestamp is under value[timeSeries][0][values][0][value][0][dateTime]
#     format is YYYY-MM-DDTHH:MM:SS.sss-05:00"
    
for site in sites:
    data = site_data[site]
    for measurement in data:
        if measurement != "siteName":
            print(f"{measurement},siteID={site},siteName='{data['siteName'][:-4].title()}' value={data[measurement]}")
