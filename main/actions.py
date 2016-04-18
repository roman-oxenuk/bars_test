#coding:utf-8
import objectpack
from m3.actions import Action, ActionPack
from m3.actions.results import OperationResult

from .models import Person, Organization
from .ui import PersonAddWindow, OrganizationAddWindow


class OrganizationPack(objectpack.tree_object_pack.TreeObjectPack):

    model = Organization

    add_to_menu = True
    add_to_desktop = True

    add_window = edit_window = OrganizationAddWindow


class PersonPack(objectpack.ObjectPack):

    model = Person

    add_to_menu = True
    add_to_desktop = True

    add_window = edit_window = PersonAddWindow
