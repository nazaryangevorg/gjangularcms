from django.db import models

class Singer(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    style = models.CharField(max_length = 100)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
