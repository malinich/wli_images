import cloudinary
import cloudinary.uploader


class Uploader:
    @classmethod
    async def upload(cls, filename, body):
        return cloudinary.uploader.upload(body)