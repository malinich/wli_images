from datetime import datetime
from umongo import Document, fields

from app import MetaBaseTemplate


class ImageDocument(Document, metaclass=MetaBaseTemplate):
    public_id = fields.StringField(required=True)
    filename = fields.StringField()
    tags = fields.ListField(fields.StringField, missing=list)
    url = fields.UrlField(required=True)
    signature = fields.StringField()
    etag = fields.StringField()

    user = fields.UUIDField(required=True)
    liked = fields.IntegerField(missing=0)
    created_at = fields.DateTimeField(missing=datetime.utcnow)

    class Meta:
        collection_name = "images"

    #  'format': 'jpg',
    #  'height': 1200,
    #  'original_filename': 'wallpaper-451535',
    #  'placeholder': False,
    #  'public_id': 'wlb7tba0cwxxhqbpbxhg',
    #  'resource_type': 'image',
    #  'secure_url': 'https://res.cloudinary.com/dib1jycri/image/upload \
    #  /v1513285833/wlb7tba0cwxxhqbpbxhg.jpg',
    #  'signature': '9202ded544547686c88efd7b61751c743c820813',
    #  'tags': [],
    #  'type': 'upload',
    #  'url': 'http://res.cloudinary.com/dib1jycri/image/upload/v1513285833
    # /\wlb7tba0cwxxhqbpbxhg.jpg',
    #  'version': 1513285833,
    #  'width': 1920}
