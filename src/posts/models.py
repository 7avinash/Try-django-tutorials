from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique = True)
    image = models.FileField(null = True, blank = True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, auto_now_add = False)
    update = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __unicode__(self):
        return self.title


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	query = Post.objects.filter(slug = slug).order_by("-id")
	exist = query.exists()
	if exist:
		new_slug = "%s-%s" %(slug, query.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug


def pre_save_post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciever, sender=Post)