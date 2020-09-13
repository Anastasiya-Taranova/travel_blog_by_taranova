from apps.onboarding.models import AuthProfile
from apps.onboarding.utils.xmodels import a
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthProfile
        fields = [a(_f) for _f in (AuthProfile.verification_code, AuthProfile.user)]
        read_only_fields = [
            a(_f)
            for _f in (
                AuthProfile.verification_code,
                AuthProfile.verified_at,
            )
        ]
