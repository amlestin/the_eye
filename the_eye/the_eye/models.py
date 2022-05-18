from django.db import models

# Create event model
class Event(models.Model):
    session_id = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    data = models.JSONField()
    timestamp = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['timestamp']
