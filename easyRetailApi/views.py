
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class HomeView(TemplateView):
    def get(self, request):
        admin_url = request.build_absolute_uri("admin")
        docs_url = request.build_absolute_uri("swagger")
        # docs_url = request.build_absolute_uri("redoc")
        # if settings.DEBUG:
        #     docs_url = request.build_absolute_uri("swagger")
        # else:
        #     docs_url = request.build_absolute_uri("redoc")
        context = {
            "admin_url": admin_url,
            "docs_url": docs_url,
        }

        return render(request, "home.html", context)


home = HomeView.as_view()