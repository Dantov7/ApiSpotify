import json


def save(*items):
    data={}
    with open ("Json.json","w") as file:
        
        for key in items:
            json.dump(data[key], file)
    
