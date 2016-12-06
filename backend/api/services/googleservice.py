from api import mapping
import requests

def finddistance(location):
    try:
        total = len(location)
        origin = "{},{}".format(location[0]['latitude'], location[0]['longitude'])
        destination = "{},{}".format(location[total-1]['latitude'], location[total-1]['longitude'])
        print total,origin, destination
        if total > 2:
            waypoints = ''
            for i in range(1,total-1):
                waypoints += "via:{}%2C{}%7C".format(location[i]['latitude'], location[i]['longitude'])
            ans = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&waypoints={}'.format(origin,destination,waypoints))
        else:
            ans = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}'.format(origin,destination))

        distance = ans.json()['routes'][0]['legs'][0]['distance']['text']
        time = ans.json()['routes'][0]['legs'][0]['duration']['text']
        # https://maps.googleapis.com/maps/api/directions/json?origin=40.6913846,-73.9896936&destination=40.6914541,-73.9897761&waypoints=via:40.6914541%2C-73.9897761
        
        return dict(distance = distance,time=time,stops=total,latitude=location[0]['latitude'],longitude=location[0]['longitude'])

    except Exception as e:
        print e
        return dict()
