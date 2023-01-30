import json


def save(*items):

    data=[]

    for i in items:
        data.append(i)

    with open ("Json.json","w") as file:
        json.dump(data, file, indent=3)
    
