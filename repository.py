# location class with attributes of latitude, longitude, and label for each point
class location:
    def __init__(self, lat, lon, text):
        self.lat = lat
        self.lon = lon
        self.text = text
        
#example points for map plotting (yes, these are actually the corresponding buildings)
codeDay = location(40.6934372, -73.9867311, 'codeDay')
sb1 = location(40.6939235, -73.9868058, 'Star Bucks')
chpt1 = location(40.6935922, -73.9863780, 'Chiptole')
pnbrd1 = location(40.6925914, -73.9884792, 'Panera Bread')

# calculated average position for all points, used later for map centering
num = 4
avgLat = (codeDay.lat + sb1.lat + chpt1.lat + pnbrd1.lat)/num
avgLon = (codeDay.lon + sb1.lon + sb1.lon + pnbrd1.lon)/num
