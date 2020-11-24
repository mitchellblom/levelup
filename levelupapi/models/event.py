from django.db import models
from django.db.models.deletion import CASCADE


class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=CASCADE)
    organizer = models.ForeignKey("Gamer", on_delete=CASCADE, related_name="events", related_query_name="event")
    description = models.TextField()
    date = models.DateField(default="2021-08-14")
    time = models.TimeField(default="19:30")

    participants = models.ManyToManyField(
        "Gamer", 
        related_name="participant_events",
        related_query_name="participant_event"
    )