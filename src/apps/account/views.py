from apps.account.forms import CreateTripForm
from apps.account.models import Trips
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

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


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = "trips_detailed"
    template_name = "account/trips_detailed.html"
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["community_trips"] = render_community_trips(request)
        context["trips"] = self.clean_object(request)
        context["trips_total"] = len(render_user_trips(request))
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
    template_name = "account/create_trip.html"
    object = Trips
    model = Trips
    fields = "__all__"

    # def get(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Trips, slug=slug_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(LoginRequiredMixin, UpdateView):
    http_method_names = ["get"]
    model = Trips
    form_class = CreateTripForm
    template_name = "account/create_trip.html"


class DeleteTrip(LoginRequiredMixin, DeleteView):
    http_method_names = ["post"]
    model = Trips
    success_url = reverse_lazy("account:trips_list")


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = "trips"
    template_name = "account/trips_list.html"

    def get_queryset(self):
        qs = Trips.objects.filter(user_id=self.request.user)
        return qs
