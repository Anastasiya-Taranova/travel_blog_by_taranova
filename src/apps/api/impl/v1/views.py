from apps.api.impl.v1.serializers import UserSerializer
from apps.onboarding.models import AuthProfile
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = AuthProfile.objects.all()
    serializer_class = UserSerializer
