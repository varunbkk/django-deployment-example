from django import template

register = template.Library()

# We definite a function works as a customer filter
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# We register the cut function
# The first one is the string that you use as part of the template tag
# The second is the function itself, also cut in this case
register .filter('cut',cut)
