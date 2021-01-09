from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    GEARS = 'gears'
    GAMING = 'gaming'
    ENTERTAINMENT = 'entertainment'
    PRODUCT_REVIEW = 'productreview'
    TECHNOLOGY = 'technology'
    DEALS = 'deals'
    TRENDING = 'trending'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    categories = models.CharField(max_length=50, choices=Categories.choices, default= Categories.GEARS)
    thumbnail = models.ImageField(upload_to='blog_photos')
    excerpts = models.CharField(max_length=150, blank=False)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
