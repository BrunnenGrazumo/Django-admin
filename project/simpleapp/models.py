from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    _author_rating = models.SmallIntegerField(default=0, db_column='author_rating')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def author_rating(self):
        return self._author_rating

    def like(self, _author_rating=_author_rating):
        self._author_rating += 1
        self.save()

    def dislike(self, _author_rating=_author_rating):
        self._author_rating -= 1
        self.save()

    def update_rating(self):
        postRating = self.post_set.aggregate(postRating=Sum("_post_rating"))
        pRat = 0
        pRat += postRating.get('postRating')

        commentRating = self.user.comment_set.aggregate(commentRating=Sum('_comment_rating'))
        cRat = 0
        cRat += commentRating.get('commentRating')

        self._author_rating = pRat*3 + cRat
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=256, unique=True)


class Post(models.Model):
    CATEGORY = (
        ("Статья", "Статья"),
        ("Новость", "Новость")
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=16, choices=CATEGORY, default='Статья')
    date_creation = models.DateTimeField(auto_now_add=True)
    category_share = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    _post_rating = models.SmallIntegerField(default=0, db_column="post_rating")


    @property
    def post_rating(self):
        return self._post_rating

    def like(self, _post_rating=_post_rating):
        self._post_rating += 1
        self.save()

    def dislike(self, _post_rating=_post_rating):
        self._post_rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123]+"..."

    def get_absolute_url(self):
        return f'/post/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    _comment_rating = models.SmallIntegerField(default=0, db_column="comment_rating")

    @property
    def comment_rating(self):
        return self._comment_rating

    def like(self, _comment_rating=_comment_rating):
        self._comment_rating += 1
        self.save()

    def dislike(self, _comment_rating=_comment_rating):
        self._comment_rating -= 1
        self.save()

