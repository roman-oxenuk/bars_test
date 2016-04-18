#coding:utf-8

from objectpack.observer import ObservableController, Observer

obs = Observer()
action_controller_registry = ObservableController(obs, '/registry_actions')
action_controller_catalog = ObservableController(obs, '/catalog_actions')
