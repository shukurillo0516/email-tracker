import os
import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.core.models import TimestampedModel
from django.contrib.auth.models import User

BASE_URL = os.environ.get("BASE_URL", "http://localhost:5050")


class Link(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="link")
    name = models.CharField(max_length=512)
    url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)


@receiver(signal=pre_save, sender=Link)
def ovveride_link_inst_url(sender, instance: Link, *args, **kwargs):
    if not instance.id:
        instance.url = f"{BASE_URL}/img/{uuid.uuid4()}.png"


class LinkRecord(TimestampedModel):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="record")
    extra_data = models.JSONField()
