import os
import uuid


def generate_upload_to(instance, filename):
    directory = str(instance.__class__.__name__.lower())
    filename, extension = os.path.splittext(filename)
    filename = str(uuid.uuid4()) + str(extension)
    return '{}/{}/{}'.format(directory, instance.id, filename)
