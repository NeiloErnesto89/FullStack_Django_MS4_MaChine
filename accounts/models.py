from django.db import models

class Mess(models.Model):
    
    name = models.CharField(max_length=20, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name
