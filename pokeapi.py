import requests
from flask import request


def retrieve_pokemons():
    offset = request.args.get('offset') or 0
    print(offset)
    url = "https://pokeapi.co/api/v2/pokemon?limit=10&offset=" + offset

    r = requests.get(url, timeout=5)
    r = r.json()
    data = r["results"]
    for idx, pokemon in enumerate(r["results"]):
        url = "https://pokeapi.co/api/v2/pokemon/" + pokemon["name"]
        r = requests.get(url, timeout=5)
        r = r.json()
        #print(r)
        image = r['sprites']['front_default']
        data[idx]["image_url"] = image
        id=r['id']
        url = "https://pokeapi.co/api/v2/pokemon-species/" + str(id)
        r = requests.get(url, timeout=5)
        r = r.json()
        print(r)
        data[idx]["image_url"] = image
        # name = r['name']
        # types = r['types'][0]['type']['name']
    return data

    #return {"id": id, "name": name, "image_url": image}
    #print(id, name, image)
    #res=jsonify({"id": id, "name": name, "image_url": image})
    #return make_response(jsonify(res), 200)