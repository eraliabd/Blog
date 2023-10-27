from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=256, )
    description = models.CharField(max_length=256, )
    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    comment_count = models.IntegerField(default=0)

    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.comment_count = self.comments.count()
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=128)
    email = models.EmailField()
    website = models.CharField(max_length=256, blank=True)
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} to {self.post.title}"

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
