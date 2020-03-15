from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import datetime

class Article(models.Model):
    title_text = models.CharField(max_length=200)
    content_path = models.FileField(upload_to='articles')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title_text
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=7) <= self.pub_date <= now

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"
@receiver(pre_delete, sender=Article)
def mymodel_delete(sender, instance, **kwargs):
    instance.content_path.delete(False)