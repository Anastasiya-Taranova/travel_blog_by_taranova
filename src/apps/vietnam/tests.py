from apps.index.views import IndexView
from django.test import Client
from django.test import TestCase


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/vietnam/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.resolver_match.app_name, "vietnam")
        self.assertEqual(resp.resolver_match.url_name, "index")
        self.assertEqual(resp.resolver_match.view_name, "vietnam:index")
        self.assertEqual(
            resp.resolver_match.func.__name__, IndexView.as_view().__name__
        )
        self.assertTemplateUsed(resp, template_name="vietnam/index.html")
