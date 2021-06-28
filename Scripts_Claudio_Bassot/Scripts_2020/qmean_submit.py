import json
import requests
import argparse
import sys

my_structure = sys.argv[1]

qmean_url = "https://swissmodel.expasy.org/qmean/submit/"

# When using Python requests - to upload from a local file, put the file in files.
# 'rb' is recommended to allow zip file upload
response = requests.post(url=qmean_url, data={"email": "claudio.bassot@scilifelab.se"}, files={"structure": open(my_structure,'rb')})

print(json.dumps(response.json(), indent=4, sort_keys=True))


current_status = requests.get(response.json()["results_json"])

print(json.dumps(current_status.json(), indent=4, sort_keys=True))
