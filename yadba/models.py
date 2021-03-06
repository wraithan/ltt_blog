from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from tagging.fields import TagField
from tagging.models import Tag


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-category-rss', kwargs={'category':self.name})

    class Meta:
        verbose_name_plural = 'Categories'


class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    draft = models.BooleanField(default=True)
    tags = TagField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)
    
    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_objects(self)

    def __unicode__(self):
        if self.draft:
            return "DRAFT -- %s -- DRAFT" % self.title
        else:
            return self.title

    def get_absolute_url(self):
        return reverse('blog-entry', kwargs={'year':self.date_posted.year, 'month':self.date_posted.month, 'slug':self.slug})

    class Meta:
        ordering = ('-date_posted',)
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'

class PoweredBy(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Project that power this one'
        verbose_name_plural = 'Projects that power this one'
