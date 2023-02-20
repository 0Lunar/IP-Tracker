from requests import get

def ip(ipaddr):
    TRACKER = "http://ip-api.com/json/" + ipaddr
    data = get(TRACKER).json()
    if(data['status'] == "success"):
        print("\n IP INFO:\n")
        print("\n [IP Adress] " + data['query'])
        print(" [Country Code] " + data['countryCode'])
        print(" [Country] " + data['country'])
        print(" [Region Code] " + data['region'])
        print(" [Region Name] " + data['regionName'])
        print(" [City] " + data['city'])
        print(" [Timezone] " + data['timezone'])
        print(" [Isp] " + data['isp'])
        print(" [Zip] " + data['zip'])
        print(" [Organization] " + data['org'])
        print(" [Latitude] " + str(data['lat']))
        print(" [Longitude] " + str(data['lon']))
        print(" [Location] " + str(data['lat']) + " " + str(data['lon']) + "\n")
    else:
        print("\n Error. ip not found")