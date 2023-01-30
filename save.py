import json


def save_in_json(*items):

    data=[]

    for i in items:
        data.append(i)

    with open ("Json.json","w") as file:
        json.dump(data, file, indent=3)
    
