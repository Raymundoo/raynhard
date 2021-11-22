# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from .models import Question, Question2, Question3, Question4

admin.site.register(Question)
admin.site.register(Question2)
admin.site.register(Question3)
admin.site.register(Question4)