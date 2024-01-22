from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, Http404
from .models import LinkRecord, Link


class LinkView(View):
    def append_link_record(self, url=None):
        link = Link.objects.filter(url__contains=url).last()
        if not link:
            return
        try:
            http_agent = self.request.META.get("HTTP_USER_AGENT")
            tzname = self.request.META.get("TZ")
            d = {}
            d["HTTP_USER_AGENT"] = http_agent
            d["tz"] = tzname
        except Exception as err:
            print(err)
            d = {}

        return LinkRecord.objects.create(extra_data=d, link=link)

    def get(self, request, url=None, *args, **kwargs):
        try:
            img_name = "1x1_%2300000000.png"
            file_type = "image/png"
            response = HttpResponse()
            response["Content-Type"] = file_type
            response["X-Accel-Redirect"] = f"/open_media/" + img_name
            response["Content-Disposition"] = "attachment;filename=" + img_name

        except Exception:
            raise Http404
        self.append_link_record(url)
        return response
