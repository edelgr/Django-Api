from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_short = models.CharField(max_length=17, default=None, null=True)
    release_date = models.DateField(blank=True, null=True)
    rating = models.FloatField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )

    def __str__(self):
        return self.title


ReactionType = (
    ('like', 'Like'),
    ('love', 'Love'),
    ('care', 'Care'),
    ('haha', 'Haha'),
    ('wow', 'Wow'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
)

class Reaction(models.Model):
    movies = models.ManyToManyField(Movie)
    reaction = models.CharField(max_length=200, default="", choices=ReactionType)

    def __str__(self):
        return 'Reaction ' + str(self.reaction)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)
