#coding:utf-8

from django.db import models


class Organization(models.Model):

    name = models.CharField(u'Наименование', max_length=255)
    inn = models.CharField(u'ИНН', max_length=12)
    kpp = models.CharField(u'КПП', max_length=9)
    parent = models.ForeignKey('Organization', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Учреждение'
        verbose_name_plural = u'Учреждения'


class Person(models.Model):

    name = models.CharField(U'Имя', max_length=255)
    surname = models.CharField(u'Фамилия', max_length=255)
    patronymic = models.CharField(u'Отчество', max_length=255)
    birth_date = models.DateField(u'Дата рождения')
    organization = models.ForeignKey(Organization, verbose_name=u'Организация')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Физ.лицо'
        verbose_name_plural = u'Физ.лица'
