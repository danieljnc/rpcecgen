from django import template
from django.utils.html import escape
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeData, mark_safe
from django.utils.text import normalize_newlines

register = template.Library()


@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def paragraphbreaks(value, autoescape=True):
    """
    Convert all newlines in a piece of plain text to HTML line breaks
    (``<br>``).
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    return mark_safe(value.replace('\n', '&lt;br&gt;'))


@register.filter
def repalcecharacters(value):
    value = value.replace('á', 'a')
    value = value.replace('Á', 'A')
    value = value.replace('é', 'e')
    value = value.replace('É', 'E')
    value = value.replace('í', 'i')
    value = value.replace('Í', 'I')
    value = value.replace('ó', 'o')
    value = value.replace('Ó', 'O')
    value = value.replace('ú', 'u')
    value = value.replace('Ú', 'U')
    value = value.replace('ü', 'u')
    value = value.replace('Ü', 'U')
    value = value.replace('>', 'greater than')
    value = value.replace('<', 'smaller than')
    value = value.replace('≥', 'greater or equal to')
    value = value.replace('≤', 'smaller or equal to')
    value = value.replace('≠', 'different to')  # check this translation
    value = value.replace('°C', 'Celsius degrees')
    # translation is needed to μ

    return value
