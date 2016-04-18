# coding: utf-8

from itertools import repeat
from spyne import srpc, Integer, Unicode, AnyDict, Array, Iterable, ComplexModel, Boolean, Date

from django.conf import settings
from .models import Organization, Person


class OrganizationModel(ComplexModel):
    organization_id = Integer
    name = Unicode


@srpc(_returns=Iterable(OrganizationModel, member_name="Organization"),
      _out_variable_name="Organizations")
def GetOrganizations():
    orgs_qs = Organization.objects.exclude(
        parent__isnull=True
    ).extra(
        select={'organization_id': 'id'}
    ).values('organization_id', 'name')
    return map(lambda org_data: OrganizationModel(**org_data), orgs_qs)


@srpc(Unicode, Unicode, Unicode, Date(format=settings.DATE_FORMAT), Integer,
    _returns=Boolean)
def CreatePerson(name, surname, patronymic, birth_date, organization_id):
    try:
        org = Organization.objects.get(pk=organization_id)
    except Organization.DoesNotExist:
        pass
    else:
        new_person = Person.objects.create(
            name=name,
            surname=surname,
            patronymic=patronymic,
            birth_date=birth_date,
            organization=org
        )
        if new_person:
            return True
    return False
