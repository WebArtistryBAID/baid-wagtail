# api.py

from django.conf import LazySettings
from rest_framework.fields import Field
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.fields import StreamValue
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.models import Image, WagtailImageFieldFile


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter("wagtailapi")

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (such as pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint("pages", PagesAPIViewSet)
api_router.register_endpoint("images", ImagesAPIViewSet)
api_router.register_endpoint("documents", DocumentsAPIViewSet)


settings = LazySettings()


class ImageUrlField(Field):
    @staticmethod
    def full_url(url):
        if hasattr(settings, "WAGTAILADMIN_BASE_URL") and url.startswith("/"):
            url = settings.WAGTAILADMIN_BASE_URL + url
        return url

    def to_representation(self, value):
        if isinstance(value, StreamValue):
            urls = []
            for image in value:
                urls.append(self.full_url(image.value.file.url))
            return urls
        else:
            return self.full_url(value.file.url)
