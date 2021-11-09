from django.urls import resolve

from assignment import settings


class PostRouter:
    route_app_labels = {'post', 'sessions', 'admin', 'auth', 'contenttypes'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'post_db'
        return

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'post_db'
        return

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels):
            return 'post_db'
        return

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'post_db'
        return

class ProductRouter:
    route_app_labels = {'product'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels):
            return 'product_db'
        return

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'product_db'
        return


