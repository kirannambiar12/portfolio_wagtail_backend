# mysite/api/graphene_wagtail.py

# Add these import statements
import graphene
from wagtail.images.models import Image
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
# Add this to the end of the file
class WagtailImageNode(DjangoObjectType):
    class Meta:
        model = Image
        # Tags would need a separate converter, so let's just
        # exclude it at this point to keep the scope smaller
        exclude_fields = ['tags']

@convert_django_field.register(Image)
def convert_image(field, registry=None):
    return WagtailImageNode(
        description=field.help_text, required=not field.null
    )

# mysite/api/graphene_wagtail.py
class WagtailImageRendition(graphene.ObjectType):
    id = graphene.ID()
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()


class WagtailImageRenditionList(graphene.ObjectType):
    rendition_list = graphene.List(WagtailImageRendition)
    src_set = graphene.String()

    def resolve_src_set(self, info):
        return ", ".join(
            [f"{img.url} {img.width}w" for img in self.rendition_list])


class WagtailImageNode(DjangoObjectType):
    class Meta:
        model = Image
        exclude_fields = ['tags']
    
    # Define all available image rendition options as arguments
    rendition = graphene.Field(
        WagtailImageRendition,
        max=graphene.String(),
        min=graphene.String(),
        width=graphene.Int(),
        height=graphene.Int(),
        fill=graphene.String(),
        format=graphene.String(),
        bgcolor=graphene.String(),
        jpegquality=graphene.Int()
    )
    rendition_list = graphene.Field(
        WagtailImageRenditionList, sizes=graphene.List(graphene.Int))

    def resolve_rendition(self, info, **kwargs):
        filters = "|".join([f"{key}-{val}" for key, val in kwargs.items()])
        img = self.get_rendition(filters)
        return WagtailImageRendition(
            id=img.id, url=img.url, width=img.width, height=img.height)

    def resolve_rendition_list(self, info, sizes=[]):
        rendition_list = [
            WagtailImageNode.resolve_rendition(self, info, width=width)
            for width in sizes
        ]
        return WagtailImageRenditionList(rendition_list=rendition_list)