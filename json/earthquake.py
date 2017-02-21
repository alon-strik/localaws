#http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson

import urllib2
import json

def printResults(data):
    theJson = json.loads(data)

    if "title" in theJson["metadata"]:
        print theJson["metadata"]["title"]

    count = theJson["metadata"]["count"]
    print str(count) + " events recorded"

    for i in theJson["features"]:
        feltResprts = i["properties"]["felt"]
        if (feltResprts != None) & (feltResprts > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " ----- Reported " + str(feltResprts)


def main():
    urlData = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'

    webUrl = urllib2.urlopen(urlData)
    print "URL code: " + str(webUrl.getcode())

    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print "Error in URL : " + str(webUrl.getcode())

if __name__ == "__main__":
    main()
