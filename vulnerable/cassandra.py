import unicodedata
from datetime import datetime

from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from django.contrib.auth import password_validation
from vulnerable.models import User as GenericUser


class Group(Model):
    name = columns.Text(
        required=True,
        # distriminator_column=True
    )

    def __str__(self):
        return self.name


class User(Model, GenericUser):
    id = columns.UUID(primary_key=True)

    EMAIL_FIELD = 'email'
    created_at = columns.DateTime(
        default=datetime.now(),
        clustering_order="DESC"
    )
    username = columns.Text(
        required=True,
        # distriminator_column=True
    )
    password = columns.Text()
    email = columns.Text()
    groups = columns.List(Group)

    def save(self, *args, **kwargs):
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None
        super(User, self).save(*args, **kwargs)
