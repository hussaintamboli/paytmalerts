import importlib


def notify(payload):
    module = importlib.import_module('paytmalerts.notifier.{}'.format(payload.pop('module')))
    return module.notify(payload)