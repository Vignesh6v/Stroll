from api import mapping

def listofTours():
    result_list = []
    result = mapping.elasticSearch('tour-index')
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            id = hit['_id']
            name = hit['_source']['name']
            createdBy = hit['_source']['createdBy']
            category = hit['_source']['category']
            time = hit['_source']['time']
            distance = hit['_source']['distance']
            stops = hit['_source']['stops']
            latitude = hit['_source']['startLocation']['latitude']
            longitude = hit['_source']['startLocation']['longitude']
            result_list.append(dict(id=id,name=name, createdBy=createdBy, category=category, time=time,distance=distance,stops=stops,latitude=latitude,longitude=longitude))
    return result_list

def specificTour(tourid):
    result = []
    # query to join tour and stops

    result.append(dict(id=tourid))
    return result

def tourTaken(tourid, userid):
    # create a entry in history table with the userid and tourid
    result = True

    return result


def createtour(tour,stops):
    # insert tour and stop records
    result = True

    return result
