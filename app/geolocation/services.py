from .models import GeolocationModel
import requests
from ..configs import API_TOKEN


class Service:

    def get_geolocation(self, ip):
        try:
            address = f"https://ipinfo.io/{ip}/json?token={API_TOKEN}"
            r = requests.get(address)
            geolocation = GeolocationModel()
            geolocation.lat, geolocation.long = r.json()["loc"].split(',')
        except:
            geolocation = {"error":True, "message": "Ip not Found"}
        return geolocation
