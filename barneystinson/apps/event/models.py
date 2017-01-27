import uuid
import datetime

from django.conf import settings

from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute, MapAttribute, BooleanAttribute


class EventModel(Model):
    type = UnicodeAttribute(hash_key=True)
    uuid = UnicodeAttribute(range_key=True, default=str(uuid.uuid4()))
    id = NumberAttribute(null=False)
    event = UnicodeAttribute(null=False)
    date = UTCDateTimeAttribute(default=datetime.datetime.now())
    payload = MapAttribute(null=False)
    read = BooleanAttribute(default=False)

    class Meta:
        table_name = settings.EVENT_LOG
        region = 'eu-west-1'