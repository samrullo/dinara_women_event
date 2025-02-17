from django import template

register = template.Library()

@register.filter
def dict_key(dictionary, key):
    """Returns the value of a dictionary given a key."""
    return dictionary.get(key, "N/A")  # Default to "N/A" if key is missing


@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to Django form fields"""
    return field.as_widget(attrs={"class": css_class})