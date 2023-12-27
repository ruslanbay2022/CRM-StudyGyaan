from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_save
from django.core.exceptions import PermissionDenied


# ЗАПРЕТ НА УДАЛЕНИЕ СУПЕРЮЗЕРА
@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
	if instance.is_superuser:
		raise PermissionDenied


# ЗАПРЕТ НА РЕДАКТИРОВАНИЕ СУПЕРЮЗЕРА
# @receiver(pre_save, sender=User)
# def save_user(sender, instance, **kwargs):
# 	if instance.is_superuser:
# 		raise PermissionDenied


# PATH TO AVATARS
def profile_avatar_path(instance: 'User', filename: str) -> str:
	return "profiles/user_{pk}/avatar/{filename}".format(
		pk=instance.user.pk,
		filename=filename,
	)


class Profile(models.Model):
	objects = models.Manager()

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	birth_date = models.DateField(null=True, blank=True)
	avatar = models.ImageField(null=True, blank=True, upload_to=profile_avatar_path)

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
