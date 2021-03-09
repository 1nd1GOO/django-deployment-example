from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This function is going to cut all the args from string value
    """
    return value.replace(arg, '')