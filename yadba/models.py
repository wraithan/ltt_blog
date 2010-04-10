from django.db import models
from tagging.fields import TagField
from tagging.models import Tag


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    tags = TagField()
    
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_objects(self)

    def __unicode__(self):
        return self.title
