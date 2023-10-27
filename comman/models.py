from django.db import models


class ContactInfo(models.Model):
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.phone


class ContactRequest(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    avatar = models.ImageField(upload_to='contactinfo/')

    name = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)

    article_title = models.CharField(max_length=256)
    article_content = models.TextField()

    twitter_url = models.CharField(max_length=256)
    facebook_url = models.CharField(max_length=256)
    linkedin_url = models.CharField(max_length=256)
    instagram_url = models.CharField(max_length=256)

    def __str__(self):
        return self.name
