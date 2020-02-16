class location:
    def __init__(self, lat, lon, text):
        self.lat = lat
        self.lon = lon
        self.text = text

codeDay = location(40.6934372, -73.9867311, 'codeDay')
#starbucks
sb1 = location(40.6939235, -73.9868058, 'Star Bucks')
#chipotle
chpt1 = location(40.6935922, -73.9863780, 'Chiptole')
#panera bread
pnbrd1 = location(40.6925914, -73.9884792, 'Panera Bread')

num = 4
avgLat = (codeDay.lat + sb1.lat + chpt1.lat + pnbrd1.lat)/num
avgLon = (codeDay.lon + sb1.lon + sb1.lon + pnbrd1.lon)/num