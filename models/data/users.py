import datetime
import mongoengine


class User(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    skills = mongoengine.ListField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
