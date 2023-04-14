from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

STYLES = [item for item in get_all_styles()]
STYLE_CHOICES = sorted([(item, item) for item in STYLES])


class Snippets(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, blank=True, default="")
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=256)
    style = models.CharField(choices=STYLE_CHOICES, default="igor", max_length=256)
    lineos = models.BooleanField(default=False)
