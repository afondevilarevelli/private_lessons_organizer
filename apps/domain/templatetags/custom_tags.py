from django.template import Library

register = Library()


@register.inclusion_tag('inclusion_tags/get_form_from_dict.html')
def get_form_from_dict(value, key):
    """Get a dict item from key"""
    return {'form': value.get(key)}
