# pylint: disable=W0212
import os
import uuid

from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile


def random_upload_path(instance, filename):
    """Return a random path to upload files
    """
    return os.path.join(
        instance._meta.object_name.lower(),
        uuid.uuid4().hex,
        filename,
    )


def get_test_image():
    """ Returns an image for running tests
    """
    io_var = BytesIO()
    size = (10, 10)
    color = (255, 0, 0, 0)

    image = Image.new('RGBA', size, color)
    image.save(io_var, format='JPEG')
    image_file = InMemoryUploadedFile(
        io_var,
        None,
        'test.jpg',
        'jpeg',
        None,
        None
    )
    image_file.seek(0)

    return image_file
