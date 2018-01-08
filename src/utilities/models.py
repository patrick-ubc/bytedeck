from utilities import forms
from django.db import models


# http://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://github.com/mixkorshun/django-safe-filefield/blob/master/safe_filefield/models.py
class RestrictedFileField(models.FileField):
    """
    Same as FileField, but you can specify:
    * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
    * max_upload_size - a number indicating the maximum file size allowed for upload.
    """

    def __init__(self, **kwargs):
        self.content_types = kwargs.pop("content_types", ["text/css"])
        self.max_upload_size = kwargs.pop("max_upload_size", 512000)

        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            form_class=forms.RestrictedFileField,

            max_upload_size=self.max_upload_size,
            content_types=self.content_types
        )

