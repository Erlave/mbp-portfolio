from django import template

register = template.Library()

@register.filter
def times(number):
    try:
        return range(int(number))
    except:
        return range(0)