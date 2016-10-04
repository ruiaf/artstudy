from django import template

register = template.Library()

def key_exists(d, key):
    res = str(key) if str(key) in d else None
    return res

def get_value(d, key):
    if str(key) in d:
        return int(d[str(key)])
    return "None"

register.filter('key_exists', key_exists)
register.filter('get_value', get_value)
