from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from users.models import User
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

STYLES = [item for item in get_all_styles()]
STYLE_CHOICES = sorted([(item, item) for item in STYLES])


class Snippets(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippet')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, blank=True, default="")
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=256)
    style = models.CharField(choices=STYLE_CHOICES, default="igor", max_length=256)
    lineos = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        lineos = 'table' if self.lineos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style,
            lineos=lineos,
            full=True,
            **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
