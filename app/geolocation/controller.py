from .services import Service

class Controller:
    service = Service()

    def get_geolocation(self, request):
        ip = request.client.host
        return self.service.get_geolocation(ip)