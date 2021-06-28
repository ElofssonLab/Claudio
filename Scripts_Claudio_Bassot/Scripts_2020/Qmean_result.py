import json
import requests

current_status = requests.get(swissmodel.expasy.org/qmean/69wdAL.json())

print(json.dumps(current_status.json(), indent=4, sort_keys=True))
