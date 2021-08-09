from django import template
from django.conf import settings
register = template.Library()

@register.filter
def pow(co_so, so_mu): # hàm luỹ thừa: tham số là có 2: co_so, so_mu
    return co_so**so_mu

@register.filter
def make_range(number):
    return range(1, number + 1)

@register.filter
def make_index_table(page, counter):
    # page 2, index = 0
    paginate_by = settings.PAGINATE_BY
    return paginate_by * (page - 1) + counter 

@register.filter
def change(value, changed):
    return value + changed