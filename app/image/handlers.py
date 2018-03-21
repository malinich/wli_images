import json
from typing import Any

import pymongo
import tornado.web
from tornado.escape import to_basestring

from image.models import ImageDocument
from utils import Routers


@Routers("/upload")
class ImageUpload(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.payload("user")
        return to_basestring(user) if user else None

    async def post(self, *args, **kwargs):
        images = []
        tags = self.transform_tags(self.payload('tags'))

        for file in self.request.files['data']:
            uploaded_file = await self.application.uploader.upload(
                file['filename'], file['body'])
            data = {
                'public_id': uploaded_file['public_id'],
                'filename': file['filename'],
                'tags': tags,
                'etag': uploaded_file['etag'],
                'created_at': uploaded_file['created_at'],
                'url': uploaded_file['url'],
                'signature': uploaded_file['signature'],
                "user": self.get_current_user(),
            }
            images.append(str(
                (await ImageDocument(**data).commit()).inserted_id))
        self.write(json.dumps(images))

    def payload(self, key: str) -> Any:
        data = self.request.body_arguments
        res = data.get(key)[0]
        return res

    @staticmethod
    def transform_tags(string_tags: bytes) -> list:
        tags = string_tags.split(b",")
        return tags


@Routers("/")
class ImageList(tornado.web.RequestHandler):

    async def get(self, *args, **kwargs):
        limit = self.get_argument("limit", 2)
        images = []
        cursor = ImageDocument \
            .find({"liked": {"$gte": 0}}) \
            .sort([("liked", pymongo.ASCENDING)]) \
            .limit(limit)
        docs = await cursor.to_list(None)
        images.extend(docs)
        sh = ImageDocument.Schema(many=True, strict=True)
        res = sh.dumps(images, True)
        self.write(res.data)


@Routers("/health")
class ImageHealth(tornado.web.RequestHandler):
    async def get(self):
        self.write("OK")
