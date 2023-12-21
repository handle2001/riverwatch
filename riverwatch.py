# Riverwatch
# Periodically fetch river gauge metrics from USGS
import json
import requests
import time
import re

API_URL = "https://waterservices.usgs.gov/nwis/iv/"
API_RESPONSE_FORMAT = "json"

# USGS Variable Codes:
# Source: https://help.waterdata.usgs.gov/parameter_cd?group_cd=PHY
USGS_VARIABLE_CODES = {
    "00010":"temperature",               # 00010 Temperature, degrees C
    "00045":"precipitation",             # 00045 Precipitation total, inches
    "00060":"discharge",                 # 00060 Discharge, cubic ft/s (daily mean)
    "00065":"height",                    # 00065 Gauge height, ft
    "00095":"conductance",               # 00095 Specific conductance, uS/cm@25C
    "00300":"dissolved_oxygen",          # 00300 Dissolved Oxygen, mg/L
    "00400":"pH",                        # 00400 pH, standard units
    "63160":"height_above_datum",        # 63160 Water level above NAVD 1988, in feet
    "63680":"turbidity",                 # 63680 Turbidity, in formazin nephelometric units (FNU)
}
# Get list of site codes to query for
# For now just use "03451500" French Broad at Asheville
# TODO: Put the list of sites in a file or DB table

sites = [
    "03451500", # French Broad at Asheville
    "03441000", # Davidson River at Brevard
]
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
    timeSeries = raw_data['value']['timeSeries']
    # The variable code is available in each timeSeries array element under variable->variableCode[0]->value
    # The actual value of the metric is available under values[0]->value[0]->value
    # So iterate over the timeSeries[] array, classify the metric type, and grab the value
    
    metrics = {}
    for variable in timeSeries:
        variableCode = variable['variable']['variableCode'][0]['value']
        variableValue = variable['values'][0]['value'][0]['value']
        metrics[USGS_VARIABLE_CODES[variableCode]] = variableValue
    metrics['siteName'] = timeSeries[0]['sourceInfo']['siteName']
    site_data[site] = metrics
    
for site in sites:
    data = site_data[site]
    for measurement in data:
        if measurement != "siteName":
            siteName = re.escape(data['siteName'][:-4].title())
            print(f"{measurement},siteID={site},siteName={siteName} value={data[measurement]}")
