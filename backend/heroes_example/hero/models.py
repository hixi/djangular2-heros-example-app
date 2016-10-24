from django.db import models
from django.utils.translation import gettext_lazy as _


class Hero(models.Model):
    # id = models.AutoField(_('id'))  # -> auto-generated by Django
    name = models.CharField(_('name'), max_length=200)

    def __str__(self):
        return self.name