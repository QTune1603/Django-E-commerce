class MicroserviceRouter:
    def db_for_read(self, model, **hints):
        return self.get_db(model)

    def db_for_write(self, model, **hints):
        return self.get_db(model)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        target_db = self.get_db_label(app_label)
        return db == target_db

    def get_db(self, model):
        if hasattr(model, '_meta'):
            return self.get_db_label(model._meta.app_label)
        elif hasattr(model, 'app_label'):
            return self.get_db_label(model.app_label)
        else:
            raise ValueError(f"Invalid model: {model}")

    def get_db_label(self, app_label):
        if app_label in ['auth', 'admin', 'sessions', 'contenttypes', 'allauth', 'account', 'socialaccount']:
            return 'default'
        elif app_label in ['cart']:
            return 'cart'
        elif app_label in ['order']:
            return 'order'
        elif app_label in ['payment']:
            return 'payment'
        elif app_label in ['shipment']:
            return 'shipment'
        elif app_label in ['comment_recommendation']:
            return 'comment'
        elif app_label in ['accounts', 'customer', 'book']: 
            return 'default'
        return 'default'


    
    def allow_relation(self, obj1, obj2, **hints):
        try:
            db1 = self.get_db(obj1._meta)
            db2 = self.get_db(obj2._meta)
            # Cho phép quan hệ giữa các DB mặc định và microservice
            if db1 == db2:
                return True
            if 'default' in {db1, db2}:
                return True
            return False
        except Exception as e:
            print("allow_relation error:", e)
            return None
