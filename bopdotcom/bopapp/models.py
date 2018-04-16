# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# User Profile model extensions referenced/used from:
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# Credit: Vitor Freitas for the resource
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	userName = models.CharField('userName', max_length=256, blank=True)
	firstName = models.CharField('firstName', max_length=256, blank=True)
	lastName = models.CharField('lastName', max_length=256, blank=True)
	birthDate = models.DateTimeField(auto_now_add=True)
	profilePicture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

class Achievement(models.Model):
	description = models.CharField('description', max_length=512, blank=True)

class Has_Achievement(models.Model):
	achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, null=False)
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
	dateUnlocked = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
	user1 = models.ForeignKey(Profile, related_name='user1', on_delete=models.CASCADE, null=False)
	user2 = models.ForeignKey(Profile, related_name='user2', on_delete=models.CASCADE, null=False)
	dateCreated = models.DateTimeField(auto_now_add=True)

class Bop(models.Model):
	message = models.CharField('message', max_length=512, blank=True)
	dateBopped = models.DateTimeField(auto_now_add=True)

class Bop_User(models.Model):
	bop = models.ForeignKey(Bop, on_delete=models.CASCADE, null=False)
	userFrom = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE, null=False)
	userTo = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE, null=False)

class Group(models.Model):
	groupName = models.CharField('name', max_length=512, blank=True)
	dateCreated = models.DateTimeField(auto_now_add=True)

class In_Group(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)
	group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)
	joined = models.DateTimeField(auto_now_add=True)

# Create a new Profile instance and attach it to Django's default user profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
