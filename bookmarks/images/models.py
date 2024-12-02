from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from blog.models import Post, Recipe

BLOG_TYPES =(
    ('breakfast','Breakfast'),
    ('lunch','Lunch'),
    ('dinner','Dinner'),
    ('travelPost','TravelPost'),
    ('moviePost','MoviePost'),
    ('dietPost','DietPost'),
             
)

CUISINE_TYPES =(
    ('indian','Indian'),
    ('thai','Thai'),
    ('american','American')
                 
)


class Image(models.Model):
    class Status(models.TextChoices):
        RECIPE = 'RE', 'recipe'
        POST = 'PO', 'post'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='images_created',
        on_delete=models.CASCADE,
    )

    category = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.RECIPE
    )
    if category =="recipe":
        recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_images'
    )
    elif category =="post":
        post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_images'
    )

    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    blogType=models.CharField(max_length=50,choices=BLOG_TYPES,default='breakfast')      
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='images_liked',
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

class Bookmark(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='images_created_recipes',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    bookmarked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =('user','recipe','image_url')
    
    def __str__(self):
        return f"{self.user.username} bookarked {self.image_url} for {self.recipe.title}"
    