import importlib
import pkgutil
import logging

plugins = []

def load_all_plugins():
    plugins.clear()
    for finder, name, ispkg in pkgutil.iter_modules(['plugins']):
        try:
            module = importlib.import_module(f'plugins.{name}')
            for attr in dir(module):
                obj = getattr(module, attr)
                if hasattr(obj, "__bases__") and "BasePlugin" in [c.__name__ for c in obj.__bases__]:
                    plugins.append(obj())
        except Exception as e:
            logging.warning(f"Impossible de charger le plugin {name}: {e}")