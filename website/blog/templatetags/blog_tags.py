from django import template
from ..models import Entry,Category,Tag

register = template.Library()

@register.simple_tag
def get_recent_entries(num=5):
    return Entry.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_popular_entries(num=5):
    return Entry.objects.all().order_by('-visiting')[:num]  # 最欢迎文章排序

# 博客分类
@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_entry_count_of_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()

#  博客归档
@register.simple_tag
def archives():
    return Entry.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_entry_count_of_date(year,month):
    return Entry.objects.filter(created_time__year=year,created_time__month=month).count()

#  标签云
@register.simple_tag
def get_tags():
    return Tag.objects.all()