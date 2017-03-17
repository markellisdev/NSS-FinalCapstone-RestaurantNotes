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
    note_text = models.CharField(max_length=250, blank=True)
    restaurant_id = models.CharField(blank=True, max_length=100)
    favorite_dish = models.CharField(default='favorite dish', max_length=100)
    # user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

class Customer(models.Model):
	"""
	Extends :model:`auth.User`
	author: Mark Ellis
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=240)
	city = models.CharField(max_length=55)
	state_province = models.CharField(max_length=55)
	country = models.CharField(max_length=55)
