from django.db import models

# Create your models here.
class Egg(models.Model):
    score = models.IntegerField(default=1000000)

    def __unicode__(self):
        return "egg <{0} hits>".format(self.score)