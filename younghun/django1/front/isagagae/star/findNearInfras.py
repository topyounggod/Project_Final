from pymongo import MongoClient

def nearInfras(latlng):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['fin']
    infras = []
    lng = latlng[1]
    lat = latlng[0]
    center = (lng, lat)
    infraName = db.list_collection_names()
    for infra in infraName:
        collection_db = db[infra]
        if infra == 'park' or infra == 'play' or infra == 'restaurant':
            c = list(collection_db.aggregate(
                [{
                    "$geoNear": {
                        "near": {"type": "Point", "coordinates": center},
                        "distanceField": 'meters',
                        "maxDistance": 2000
                    }
                }]
            ))
        else:
            c = list(collection_db.aggregate(
                [{
                    "$geoNear": {
                        "near": {"type": "Point", "coordinates": center},
                        "distanceField": 'meters',
                        "maxDistance": 1000
                    }
                }]
            ))
        if c:
            for one in c:
                infras.append(one)
    return infras