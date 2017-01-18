import os
import uuid

from django.db import models


class ImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        model_name = str(instance.__class__.__name__.lower())
        model_field_name = str(self.name)
        filename, extension = os.path.splitext(filename)
        filename = str(uuid.uuid4()) + str(extension)
        return '{}/{}/{}/{}'.format(model_name, model_field_name, instance.id, filename)