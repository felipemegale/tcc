import pandas as pd
import json


with open("osm_start.out") as st_head:
    jsons = [json.loads(line) for line in st_head]

    for obj in jsons:
        print(obj["address"])
