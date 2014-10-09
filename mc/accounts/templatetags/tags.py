from django import template

register = template.Library()

@register.simple_tag
def active_step(*fields):
    for field in fields:
        if not field:
            return ''
    return 'active'

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def karma(cooperative, num):
    step = 0
    if cooperative.nombre and cooperative.descripcion:
        step = step + 1
    if cooperative.objeto:
        step = step + 1
    if cooperative.direccion and cooperative.localidad and cooperative.provincia and cooperative.codigo_postal:
        step = step + 1
    if step > num:
        return 'active'
    return ''

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range( value )