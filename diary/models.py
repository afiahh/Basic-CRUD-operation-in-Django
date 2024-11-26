from django.db import models
from django.utils.timezone import now

# Create your models here.


class DiaryEntry(models.Model):
    MOODS = [
        ("😊", "Happy"),
        ("😢", "Sad"),
        ("😡", "Angry"),
        ("🤔", "Thoughtful"),
        ("😄", "Excited"),
        ("😴", "Sleepy"),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    mood = models.CharField(max_length=2, choices=MOODS,blank=True,null=True,default="😴")
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} ({self.mood})"

