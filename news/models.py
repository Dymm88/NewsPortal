from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse

news = 'nw'
article = 'ar'

HEADER = [
    (news, 'новость'),
    (article, 'статья'),
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name

    def update_rating(self):
        articles = Post.objects.filter(author=self)
        article_rating = articles.aggregate(Sum('rating')).get('rating__sum') * 3
        comments = Comment.objects.filter(user=self.user)
        comment_rating = comments.aggregate(Sum('rating')).get('rating__sum')
        others_comments = Comment.objects.filter(post__author=self)
        others_comments_rating = others_comments.aggregate(Sum('rating')).get('rating__sum')
        overall = sum((article_rating, comment_rating, others_comments_rating))
        self.rating = overall
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice = models.CharField(max_length=2, choices=HEADER, default=news)
    date_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]} + {...}'

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
