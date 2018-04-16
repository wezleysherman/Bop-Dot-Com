# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(In_Group)
admin.site.register(Bop)
admin.site.register(Bop_User)
admin.site.register(Friend)
admin.site.register(Achievement)
admin.site.register(Has_Achievement)