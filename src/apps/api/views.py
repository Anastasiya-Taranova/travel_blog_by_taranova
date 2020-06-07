from rest_framework.authtoken.views import ObtainAuthToken as _DrfObtainAuthToken


class ObtainAuthToken(_DrfObtainAuthToken):
    swagger_schema = None
