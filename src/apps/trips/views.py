from django.views.generic import DetailView

from apps.trips.models import Countries


class Count(DetailView):
    template_name = "trips/index.html"
    model = Countries

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        js = []
        markers = []

        for i, point in enumerate(self.object.marker_map.all()):
            marker = f"marker{i}"
            js.append(f"{marker}=DG.marker([{point.geolocation}]).addTo(map);")
            markers.append(marker)

        js = "\n".join(js)

        markers = ",".join(markers)
        js = f"{js}\ngroup = DG.featureGroup([{markers}]);"

        ctx["markers_js"] = js

        return ctx
