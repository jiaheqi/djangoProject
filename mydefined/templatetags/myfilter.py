from django import template
register = template.Library()

@register.filter(name='my_replace')
def do_replace(value, args):
    oldValue = args.split(':')[0]
    newValue = args.split(':')[1]
    return value.replace(oldValue, newValue)