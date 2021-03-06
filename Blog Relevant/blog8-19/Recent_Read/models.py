from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# Create your models here.


class Recent_Read(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    Read_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_delete = models.BooleanField(default=False)
    class Meta:
        ordering = ['-Read_time']
