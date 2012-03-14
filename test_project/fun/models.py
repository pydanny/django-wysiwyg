from django.db import models


class Playground(models.Model):
    body = models.TextField()


class FancyPlayground(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
