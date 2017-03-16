from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class RestaurantNote(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    note_text = models.TextField()
    restaurant_id = models.CharField()
    favorite_dish = models.CharField(default='favorite dish', max_length=100)
    user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)