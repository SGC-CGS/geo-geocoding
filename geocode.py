import pandas as pd
import requests as req
import numpy as np

addr = pd.read_csv('./source/google_rerun.csv')

addr["google_type"] = None
addr["google_latitude"] = 0
addr["google_longitude"] = 0

# Google maps
key = "AIzaSyDetnKxVhUlIvPa-oWaEF69txOeidVzc4U"
url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}"

# Pelias
# url = "http://3.96.64.61:4000/v1/search?text={0}&boundary.country=CAN"

# ADDRESS	CITY	POSTALCODE	POBOX	PROVINCE
# 729 GLENWOOD AVE	KELOWNA	V1Y5M4		British Columbia

for index, row in addr.iterrows():
    target = row["address"]

    if not isinstance(target, str):
        addr.loc[index, 'google_type'] = ""
        addr.loc[index, 'google_latitude'] = ""
        addr.loc[index, 'google_longitude'] = ""

        print("Skipping index " + str(index) + " because address is empty.")

        continue;


    # Google Maps
    r = req.get(url.format(target, key))

    # PELIAS PROCESSING
    # r = req.get(url.format(target))

    # results = r.json()["features"]

    # if len(results) == 0:
    #    continue

    # exact = list(filter(lambda x: (x["properties"]["match_type"] == "exact"), results))

    # prioritize exact matches first
    # if len(exact) > 0:
    #    results = exact

    # for r in results:
    #    r = max(results, key=lambda x: (x["properties"]["confidence"]))

    # geo = r["geometry"]["coordinates"]
    # END OF PELIAS PROCESSING

    # GOOGLE MAPS PROCESSING
    results = r.json()["results"]

    if len(results) == 0:
        continue

    byType = {
        "ROOFTOP": [],
        "RANGE_INTERPOLATED": [],
        "GEOMETRIC_CENTER": [],
        "APPROXIMATE": []
    }

    for r in results:
        geo = r["geometry"]
        type = geo["location_type"]
        byType[type].append({"lat": geo["location"]["lat"], "lon": geo["location"]["lng"]})

    best = None

    if len(byType["ROOFTOP"]) > 0:
        best = "ROOFTOP"

    elif len(byType["RANGE_INTERPOLATED"]) > 0:
        best = "RANGE_INTERPOLATED"

    elif len(byType["GEOMETRIC_CENTER"]) > 0:
        best = "GEOMETRIC_CENTER"

    elif len(byType["APPROXIMATE"]) > 0:
        best = "APPROXIMATE"

    addr.loc[index, 'google_type'] = best
    addr.loc[index, 'google_latitude'] = byType[best][0]["lat"]
    addr.loc[index, 'google_longitude'] = byType[best][0]["lon"]

    print("Geocoding " + target + " done.")

addr.to_csv("./geocoded/google_run.csv", index=False)
