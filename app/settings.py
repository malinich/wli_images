import os

import consul

from errors import ImpropertyConfigured

PORT = os.environ.get("PORT", 3000)

DB_NAME = "wli"
_SERVICE_KEY_PREFIX = "wli"
CONSUL_HOST = os.environ.get("CONSUL_HOST", 'localhost')
CONSUL_IMAGE_NAME = str.join('.', [_SERVICE_KEY_PREFIX, "image"])

_MONGO_SERVICE_NAME = 'mongo'

consul_client = consul.Consul(CONSUL_HOST)


def get_discovery_service(consul_client, service_name):
    return consul_client.agent.service.agent.catalog.service(service=service_name)


_, mongodb_data = get_discovery_service(consul_client, _MONGO_SERVICE_NAME)

if not mongodb_data:
    raise ImpropertyConfigured("MongoDB not running")

MONGODB_URI = 'mongodb://{address}:{port}/{db}'.format(
    address=mongodb_data[0]['Address'],
    port=mongodb_data[0]["ServicePort"],
    db=DB_NAME
)

APPS = (
    "image",
)

CLOUDINARY = {
    'cloud_name': 'dib1jycri',
    'api_key': '178382392551894',
    'api_secret': 'QYakHqd5ps9PYMPapMajLWVHrOk',
}
