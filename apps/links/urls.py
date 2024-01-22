from django.urls import path
from .views import *

app_name = "links"


urlpatterns = [path("<path:name>", LinkView.as_view(), name="link_view")]
