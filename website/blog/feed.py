from django.contrib.syndication.views import Feed
from .models import Entry

#  RSS订阅
class LatesEntriesFeed(Feed):
    title = 'linguiyi的博客'
    link = '/siteblogs/'
    description = 'linguiyi的最新博客文章!'

    def items(self):
        return Entry.objects.order_by('-created_time')[:5]

    def item_title(self,item):
        return item.title
    def item_description(self, item):
        return item.abstract
