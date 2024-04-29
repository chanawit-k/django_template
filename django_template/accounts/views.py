from django.views.generic import TemplateView

# Create your views here.
class SampleView(TemplateView):
    template_name = "accounts/sample_html.html"

