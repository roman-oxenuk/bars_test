# coding: utf-8

from django.conf import urls

from objectpack import desktop

import actions
import controller


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return urls.patterns(
        "",
        controller.action_controller_registry.urlpattern,
        controller.action_controller_catalog.urlpattern,
    )


def register_actions():
    """
    регистрация экшенов
    """
    controller.action_controller_registry.packs.extend([
        actions.PersonPack(),
    ])
    controller.action_controller_catalog.packs.extend([
        actions.OrganizationPack(),
    ])


def register_desktop_menu():
    """
    регистрация элеметов рабочего стола
    """
    desktop.uificate_the_controller(
        controller.action_controller_registry,
        menu_root=desktop.MainMenu.SubMenu(u'Реестры')
    )
    desktop.uificate_the_controller(
        controller.action_controller_catalog,
        menu_root=desktop.MainMenu.SubMenu(u'Справочники')
    )
