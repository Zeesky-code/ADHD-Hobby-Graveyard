from django.db import models

# Create your models here.

class Hobby(models.Model):
    title = models.CharField(max_length=200)
    Faded = models.BooleanField(default=False)
    created =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.title