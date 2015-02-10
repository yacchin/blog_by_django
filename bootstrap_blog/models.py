from django.db import models
from django.utils.encoding import smart_unicode


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return smart_unicode(self.name)


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return smart_unicode(self.name)


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')

    def __unicode__(self):
        return smart_unicode(self.title)


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_at = models.DateTimeField('date published')

    def __unicode__(self):
        return smart_unicode(self.body)


class PostsTags(models.Model):
    post = models.ForeignKey(Post)
    tag = models.ForeignKey(Tag)
