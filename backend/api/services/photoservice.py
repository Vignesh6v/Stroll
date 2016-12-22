from api import mapping
from time import gmtime, strftime

def getPhotos(stopid):
    try:
        photolist = []
        body = {"query": {"match_phrase": {"stopId":stopid}}}
        result = mapping.elasticSearch('photo-index',body)
        hits = result['hits']['hits']
        if hits:
            for hit in hits:
                _id = hit['_id']
                comment = hit['_source']['name']
                userName = getUserName(hit['_source']['userId'])
                postedOn = hit['_source']['postedOn']
        comments.append(dict(commentid=_id,stopId=stopid,comments=comment,userName=userName,postedOn=postedOn))
    except Exception as e:
        return []
    return photolist
