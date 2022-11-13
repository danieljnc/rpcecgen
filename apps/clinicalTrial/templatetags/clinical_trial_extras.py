from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def assign_class(value):
    """
    Convert all newlines in a piece of plain text to HTML line breaks
    (``<br>``).
    """
    if value == '' or value is None:
        return 'tr-missing_color'
    else:
        print(f'Type: {type(value)}, value {value}')
        if isinstance(value, datetime):
            value = str(value)
        value = value.strip().lower()

        if value != 'no procede' and value != 'not applicable' and value != 'not apply' and value != 'none' and value != 'no proceed' and value != 'no proceed.':
            return 'ct-body3 tr-rowBody'
        else:
            return 'tr-missing_color'
