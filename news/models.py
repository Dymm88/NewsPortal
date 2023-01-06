from django.contrib.auth.models import User
from django.db import models

new = 'nw'
article = 'ar'

CHOICE_TEXT = [
    (new, 'Новость'),
    (article, 'Статья'),
]


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = 'Post.post_rating' * 3 + 'Comment.comment_rating'
        return self.author_rating


class Category(models.Model):
    sport = models.CharField(max_length=150, unique=True)
    science = models.CharField(max_length=150, unique=True)
    politic = models.CharField(max_length=150, unique=True)
    crime = models.CharField(max_length=150, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice_field = models.CharField(max_length=2, choices=CHOICE_TEXT, default='nw')
    time_add = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=100)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        return

    def dislike(self):
        self.post_rating -= 1
        return

    def preview(self):
        return f'{self.text[:123]}{...}'

    def __str__(self):
        return f'{self.author}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=500)
    comment_add = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        return

    def dislike(self):
        self.comment_rating -= 1
        return
