import networkx as nx
import json
import requests

dockless_api = "https://data.austintexas.gov/resource/7d8e-dm7r.json"


def getAPI():
    response = requests.get(dockless_api)

    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return "Erro na requisicao"


if __name__ == "__main__":
    data = getAPI()
    
    file = open("data.json", "w")
    file.write(json.dumps(data, indent=4))
    file.close()
