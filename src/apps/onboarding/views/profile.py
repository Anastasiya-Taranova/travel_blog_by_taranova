from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from apps.onboarding.models import Trips
from apps.onboarding.models import UserNotifications

User = get_user_model()


def render_community_trips(request):
    community_trips = []
    for trip in Trips.objects.all():
        if trip.public:
            if trip.user_id.get_username() != request.user.get_username():
                community_trips.append(trip)
    return community_trips


def render_user_trips(request):
    trips = []
    for trip in Trips.objects.all():
        if trip.user_id.get_username() == request.user.get_username():
            trips.append(trip)
    return trips


def render_user_notifications(request):
    notifs = []
    for notif in UserNotifications.objects.all():
        if notif.user_id.get_username() == request.user.get_username():
            notifs.append(notif)
    return notifs


class ProfileView(TemplateView):
    template_name = "onboarding/me.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        req = self.request

        try:
            profile = req.user.profile
        except (User.profile.RelatedObjectDoesNotExist, AttributeError):
            profile = None

        ctx["profile"] = profile

        newbie = (req.GET or {}).get("newbie")
        if newbie:
            ctx["newbie_alert"] = " ".join(
                (
                    "We strongly encourage you to update your profile and password!",
                    "Your current password is the same as your current username.",
                    "Please copy the username, set the new one, and update the password.",
                )
            )

        return ctx


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = "trips_detailed"
    template_name = "onboarding/trips_detailed.html"
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["community_trips"] = render_community_trips(request)
        context["trips"] = self.clean_object(request)
        context["notifs"] = render_user_notifications(request)
        context["trips_total"] = len(render_user_trips(request))
        context["notifs_total"] = len(render_user_notifications(request))
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Trips, slug=slug_)

    def clean_object(self, request):
        slug_ = self.kwargs.get("slug")
        obj = self.get_object()
        if obj.user_id.get_username() == request.user.get_username() or obj.public:
            return get_object_or_404(Trips, slug=slug_)
        else:
            return render(
                request,
                "index/index.html",
                {
                    "error": "This is a private trip which you "
                    "do not have permissions to view."
                },
            )


class CreateTrip(LoginRequiredMixin, CreateView):
    context_object_name = "create_trip"
    template_name = "onboarding/create_trip.html"
    object = Trips
    model = Trips
    fields = "__all__"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notifs"] = render_user_notifications(request)
        context["notifs_total"] = len(render_user_notifications(request))
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Trips, slug=slug_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(LoginRequiredMixin, UpdateView):
    context_object_name = "update_trip"
    template_name = "onboarding/create_trip.html"
    model = Trips
    fields = "__all__"

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trips"] = self.get_object()
        context["notifs"] = render_user_notifications(request)
        context["notifs_total"] = len(render_user_notifications(request))
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Trips, slug=slug_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(LoginRequiredMixin, DeleteView):
    context_object_name = "update_trip"
    template_name = "onboarding/create_trip.html"
    model = Trips
    success_url = reverse_lazy("onboarding:trips_list")

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Trips, slug=slug_)

    def post(self, request, *args, **kwargs):
        pass


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = "trips_list"
    template_name = "onboarding/trips_list.html"
    object_list = Trips.objects.all()

    def get(self, request, *args, **kwargs):
        self.object_list = render_user_trips(request)
        context = super().get_context_data(**kwargs)
        context["trips"] = render_user_trips(request)
        context["notifs"] = render_user_notifications(request)
        context["trips_total"] = len(render_user_trips(request))
        context["notifs_total"] = len(render_user_notifications(request))
        return render(request, self.template_name, context)
