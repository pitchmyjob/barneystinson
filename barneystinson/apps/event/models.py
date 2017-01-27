from pynamodb.models import Model
from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute, MapAttribute, BooleanAttribute

from django.conf import settings


class EventModel(Model):
    type = UnicodeAttribute(hash_key=True)
    uuid = UnicodeAttribute(range_key=True)
    id = NumberAttribute(null=False)
    event = UnicodeAttribute(null=False)
    date = UTCDateTimeAttribute(null=False)
    payload = MapAttribute(null=False)
    read = BooleanAttribute(default=False)

    class Meta:
        table_name = settings.EVENT_LOG
        region = 'eu-west-1'
