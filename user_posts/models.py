from django.db import models
from django.utils import timezone


class User_Posts(models.Model):
 
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)


    def __unicode__(self):
            return self.title

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    