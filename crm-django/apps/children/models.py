from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
import os


def profile_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('children', filename)


# CLASS Child
class Child(models.Model):
    class Meta:
        verbose_name = _('child')
        verbose_name_plural = _('children')

    objects = models.Manager()
    GENDER = [
        ('M', 'Man'),
        ('W', 'Woman'),
    ]
    gender = models.CharField(verbose_name=_('Gender'), max_length=1, choices=GENDER, default='M')
    name = models.CharField(verbose_name=_('Name'), max_length=100, db_index=True)
    middlename = models.CharField(verbose_name=_('Middlename'), max_length=100, db_index=True)
    surname = models.CharField(verbose_name=_('Surname'), max_length=100, db_index=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(verbose_name=_('Photo'), null=True, blank=True, upload_to=profile_avatar_path)
    bio = models.TextField(verbose_name=_('Bio'), null=False, blank=True, db_index=True)
    addition_date = models.DateTimeField(verbose_name=_('Addition Date'), auto_now_add=True)
    archived = models.BooleanField(verbose_name=_('Archived'), default=False, null=False, blank=True)

    def __str__(self) -> str:
        return f"Child(pk={self.pk}, name={self.name!r})"
