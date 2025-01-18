from django import template 
from goods.models import Categories 


register = template.Library()

@register.simple_tag()
def tag_categories():
    return  Categories.objects.all()


from django.utils.http import urlencode

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs): 
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)