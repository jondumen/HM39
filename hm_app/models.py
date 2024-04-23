from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    activity_years = models.IntegerField()
    last_song = models.CharField(max_length=50)
    popular_song = models.CharField(max_length=50)
    # Otros campos

    # Identificadores de redes sociales
    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    youtube_channel_id = models.CharField(max_length=50, blank=True, null=True)
    soundcloud_username = models.CharField(max_length=50, blank=True, null=True)
    niconico_user_id = models.CharField(max_length=50, blank=True, null=True)
    # Otros campos de redes sociales

    def twitter_link(self):
        if self.twitter_username:
            return f"https://twitter.com/{self.twitter_username}"
        return None

    def youtube_link(self):
        if self.youtube_channel_id:
            return f"https://www.youtube.com/channel/{self.youtube_channel_id}"
        return None
    
    def soundcloud_link(self):
        if self.soundcloud_username:
            return f"https://www.youtube.com/channel/{self.soundcloud_username}"
        return None
    
    def niconico_link(self):
        if self.niconico_user_id:
            return f"https://www.youtube.com/channel/{self.niconico_user_id}"
        return None

    def __str__(self):
        return self.nombre

class Comments(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    