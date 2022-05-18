from django.db import models

# Create event model
class Event(models.Model):
    session_id = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['timestamp']
