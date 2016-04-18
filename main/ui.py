#coding:utf-8
# import objectpack
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from .models import Organization


class PersonAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PersonAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label=u'Фамилия',
            name='surname',
            allow_blank=False,
            anchor='100%')

        self.field__patronymic = ext.ExtStringField(
            label=u'Отчество',
            name='patronymic',
            allow_blank=False,
            anchor='100%')

        self.field__birth_date = ext.ExtDateField(
            label=u'Дата рождения',
            name='birth_date',
            anchor='100%')

        self.field__organization_id = make_combo_box(
            label=u'Учреждение',
            name='organization_id',
            allow_blank=False,
            anchor='100%',
            data=Organization.objects.all().values_list('pk', 'name'))

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PersonAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__patronymic,
            self.field__birth_date,
            self.field__organization_id,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PersonAddWindow, self).set_params(params)
        self.height = 'auto'


class OrganizationAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(OrganizationAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__inn = ext.ExtStringField(
            label=u'ИНН',
            name='inn',
            allow_blank=False,
            anchor='100%')

        self.field__kpp = ext.ExtStringField(
            label=u'КПП',
            name='kpp',
            allow_blank=False,
            anchor='100%')

        # self.field__parent_id = make_combo_box(
        #     label=u'Родительская орг-ция',
        #     name='parent_id',
        #     allow_blank=False,
        #     anchor='100%',
        #     data=Organization.objects.all().values_list('pk', 'name'))

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(OrganizationAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__inn,
            self.field__kpp,
            # self.field__parent_id,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(OrganizationAddWindow, self).set_params(params)
        self.height = 'auto'
