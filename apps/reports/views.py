from django.views.generic import View
from django.http import HttpResponse
from .utils import render_to_pdf
from django.conf import settings

# Create your views here.
class StatusRpcecPdf(View):

    def get(self, request, *args, **kwargs):
        img = settings.STATIC_URL + "/img/homepage.png"
        pdf = render_to_pdf('reports/status_rpcec.html', {'img': img})
        return HttpResponse(pdf, content_type="application/pdf")
