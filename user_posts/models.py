from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class User_Posts(models.Model):
 
    title = models.CharField(max_length=100, help_text='Enter post title')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)  # default = 'default.png'
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="user_likes")
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models

        # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def total_likes(self):
        return self.likes.count()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def __str__(self):
    #     return self.title

    # def snippet(self):
    #     return self.body[:50] + "..."

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    