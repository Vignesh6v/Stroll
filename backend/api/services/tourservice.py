from api import mapping
from time import gmtime, strftime

def listofTours():
    result_list = []
    result = mapping.elasticSearch('tour-index')
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            name = hit['_source']['name']
            createdBy = hit['_source']['createdBy']
            category = hit['_source']['category']
            time = hit['_source']['time']
            distance = hit['_source']['distance']
            stops = hit['_source']['stops']
            latitude = hit['_source']['latitude']
            longitude = hit['_source']['longitude']
            result_list.append(dict(tourid=_id,name=name, createdBy=createdBy, category=category, time=time,distance=distance,stops=stops,latitude=latitude,longitude=longitude))
    return result_list

def specificTour(tourid):
    stopresult = []
    tourresult = dict()
    comments = []
    body = {"query": {"match_phrase": {"_id":tourid}}}
    result = mapping.elasticSearch('tour-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            name = hit['_source']['name']
            createdBy = hit['_source']['createdBy']
            category = hit['_source']['category']
            time = hit['_source']['time']
            distance = hit['_source']['distance']
            stops = hit['_source']['stops']
            latitude = hit['_source']['latitude']
            longitude = hit['_source']['longitude']
            tourresult = dict(tourid=_id,name=name, createdBy=createdBy, category=category, time=time,distance=distance,stops=stops,latitude=latitude,longitude=longitude)

    body = {"query": {"match_phrase": {"tourId":tourid}}}
    result = mapping.elasticSearch('stops-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            name = hit['_source']['name']
            sequence = hit['_source']['sequence']
            description = hit['_source']['description']
            stop_latitude = hit['_source']['stop_latitude']
            stop_longitude = hit['_source']['stop_longitude']
            stopresult.append(dict(stopid=_id,name=name,sequence=sequence,description=description,stop_latitude=stop_latitude,stop_longitude=stop_longitude))

    body = {"query": {"match_phrase": {"stopId":tourid}}}
    result = mapping.elasticSearch('comment-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            _id = hit['_id']
            comment = hit['_source']['comments']
            userName = getUserName(hit['_source']['userId'])
            postedOn = hit['_source']['postedOn']
            comments.append(dict(commentid=_id,tourId=tourid,comments=comment,userName=userName,postedOn=postedOn))

    result = dict(tour=tourresult,stops=stopresult,comments=comments)
    return result

def tourTaken(tourid, userid):
    # create a entry in history table with the userid and tourid
    body = {"query": {"match_phrase": {"_id":userid}}}
    result = mapping.elasticSearch('user-index',body)
    result = result['hits']
    if result['total'] >= 1:
        data = dict(tourId=tourid,userId=userid,takenOn= strftime("%Y-%m-%d %H:%M:%S", gmtime()) )
        result = mapping.elasticInsert('history-index','history', data)
        if result['_id']:
            return True
        else:
            return False
    else:
        print 'No user with userid - {}'.format(userid)
        return False


def createtour(tour,stops):
    # insert tour and stop records
    # need to update for inserting photos
    try:
        result = mapping.elasticInsert('tour-index','tour', tour)
        stopids = []
        for x in stops:
            x['tourId'] = result['_id']
            stopresult = mapping.elasticInsert('stops-index','stops', x)
            stopids.append(stopresult['_id'])
        #print stopids
        result = True
    except Exception as e:
        result = False
    return result

def entercomment(stopid,data):
    #print stopid, data
    try:
        data['postedOn'] =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
        data['stopId'] = stopid
        print data
        result = mapping.elasticInsert('comment-index','comment',data)
        result = True
    except Exception as e:
        result = False
    return result

def stopdeatils(stopid):
    try:
        #print stopid
        comments = []
        body = {"query": {"match_phrase": {"stopId":stopid}}}
        result = mapping.elasticSearch('comment-index',body)
        #print result
        hits = result['hits']['hits']
        if hits:
            for hit in hits:
                _id = hit['_id']
                comment = hit['_source']['comments']
                userName = getUserName(hit['_source']['userId'])
                postedOn = hit['_source']['postedOn']
                comments.append(dict(commentid=_id,stopId=stopid,comments=comment,userName=userName,postedOn=postedOn))
    except Exception as e:
        comments = False
    return comments

def getUserName(userid):
    body = {"query": {"match_phrase": {"_id":userid}}}
    result = mapping.elasticSearch('user-index',body)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            firstName = hit['_source']['firstName']
            lastName = hit['_source']['lastName']
            break
        return str(firstName)+' '+str(lastName)
    else:
        return None
