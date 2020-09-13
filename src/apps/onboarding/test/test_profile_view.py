from apps.onboarding.utils.xtests import TemplateResponseTestMixin
from apps.onboarding.views import ProfileView
from django.test import TestCase


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/onboarding/me/",
            expected_view_name="onboarding:me",
            expected_view=ProfileView,
            expected_template="onboarding/me.html",
        )
