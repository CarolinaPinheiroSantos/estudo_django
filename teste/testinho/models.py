from django.db import models

class Carol(models.Model):

    amigos = models.CharField(max_length=50)
    familia = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Carolinas"
