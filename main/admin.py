#coding:utf-8
from django.contrib import admin

from .models import Organization, Person


admin.site.register(Organization)
admin.site.register(Person)
