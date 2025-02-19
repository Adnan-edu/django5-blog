from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly' # Change frequency of your post pages
    priority = 0.9 # And their relevance in the website (Max value is 1)

    def items(self):
        return Post.published.all() # Objects to include in this sitemap

    def lastmod(self, obj): # Receives each object returned by items() and  returns the last time the object was modified
        return obj.updated