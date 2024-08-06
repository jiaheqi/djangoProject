from djangoProject import settings

DATABASE_MAPPINGS = settings.DATABASE_APPS_MAPPING


class DbAppsRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in DATABASE_MAPPINGS:
            return DATABASE_MAPPINGS[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in DATABASE_MAPPINGS:
            return DATABASE_MAPPINGS[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = DATABASE_MAPPINGS.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPINGS.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_syncdb(self, db, model):
        if db in DATABASE_MAPPINGS.values():
            return DATABASE_MAPPINGS.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPINGS:
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in DATABASE_MAPPINGS.values():
            return DATABASE_MAPPINGS.get(app_label) == db
        elif app_label in DATABASE_MAPPINGS:
            return False
        return None
