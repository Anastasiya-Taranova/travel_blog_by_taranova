from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "onboarding/all_posts.html"
