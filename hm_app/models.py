from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    last_song = models.CharField(max_length=50)
    popular_song = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    

    # Identificadores de redes sociales
    picture_url = models.CharField(max_length=500, blank=True, null=True)
    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    youtube_channel_id = models.CharField(max_length=50, blank=True, null=True)
    niconico_user_id = models.CharField(max_length=50, blank=True, null=True)

    def picture_link(self):
        if self.picture_url:
            return f"{self.picture_url}"
        return None
    
    def twitter_link(self):
        if self.twitter_username:
            return f"https://twitter.com/{self.twitter_username}"
        return None

    def youtube_link(self):
        if self.youtube_channel_id:
            return f"https://www.youtube.com/{self.youtube_channel_id}"
        return None
    
    def niconico_link(self):
        if self.niconico_user_id:
            return f"https://www.nicovideo.jp/user/{self.niconico_user_id}"
        return None

    def __str__(self):
        return self.name

class Comments(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    