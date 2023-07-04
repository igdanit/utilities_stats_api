# SHOULD LAUNCH ONLY FOR EMPTY DATABASE.
# Create collections needed for project and indexes for them.
import sys

sys.path.append("..")

import pymongo
from config import settings

client = pymongo.MongoClient(settings.DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]
indications = db.get_collection("indications")
indication_types = db.get_collection("indicationTypes")

indications.create_index(
    [("createdAt.month", pymongo.DESCENDING), ("indicationTypeID", pymongo.ASCENDING)],
    name="indicationsIndex",
    unique=True,
)

indication_types.create_index(
    [("addressID", pymongo.ASCENDING), ("type", pymongo.ASCENDING)],
    name="indicationTypesIndex",
    unique=True,
)

indications.create_index(
    [("userID", pymongo.HASHED)],
    name="indicationUserIDIndex"
)

indication_types.create_index(
    [("userID", pymongo.HASHED)],
    name="indicationTypesUserIDIndex"
)