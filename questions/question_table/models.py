from django.db import models

MAX_CHAR_LENGTH = 200

class Question(models.Model):
    title = models.CharField(max_length=MAX_CHAR_LENGTH)
    description = models.CharField(max_length=MAX_CHAR_LENGTH)

    def __str__(self):
        return self.title
