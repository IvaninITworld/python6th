from django.views.generic import TemplateView
from django.apps import apps
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["app_list"] = ["polls", "books"]
        dicVerbos = {}
        for app in apps.get_app_configs():
            if "site-packages" not in app.path:
                dicVerbos[app.label] = app.verbos_name

        context["verbos_dict"] = dicVerbos
        return context