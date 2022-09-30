from os import environ
from delphes.models import person

DOMAIN = {
    "people": person,
}

MONGO_URI = environ.get("EVE_MONGO_URI", "mongodb://localhost")
MONGO_USERNAME = environ.get("EVE_MONGO_USERNAME", None)
MONGO_PASSWORD = environ.get("EVE_MONGO_PASSWORD", None)

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ["GET", "POST", "DELETE"]

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]
