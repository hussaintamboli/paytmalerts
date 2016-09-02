from django.db import models


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(Common):
    data = models.TextField()


class Type(Common):
    type = models.CharField(max_length=30)


class Alert(Common):
    alert_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    alert_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=255)

