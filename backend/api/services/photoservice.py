from api import mapping
import random
from time import gmtime, strftime
from sample import photos
def getPhotos(stopid):
    try:
        photolist = []
        for _ in range(5):
            i = random.randint(0, 30)
            photolist.append(str(photos[i]))
    except Exception as e:
        return []
    return photolist
