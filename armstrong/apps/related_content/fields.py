from django.contrib.contenttypes.generic import GenericRelation

from .models import RelatedContent


class RelatedContentField(GenericRelation):
    def __init__(self, **kwargs):
        defaults = {
            "object_id_field": "source_id",
            "content_type_field": "source_type",
        }
        defaults.update(kwargs)
        super(RelatedContentField, self).__init__(RelatedContent, **defaults)
        
from south.modelsinspector import add_ignored_fields
add_ignored_fields(["^armstrong\.apps\.related_content\.fields\.RelatedContentField"])