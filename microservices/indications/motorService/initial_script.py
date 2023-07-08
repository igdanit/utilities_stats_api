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

try:
    indications.create_index(
        [("createdAt.month", pymongo.DESCENDING), ("indicationTypeID", pymongo.ASCENDING)],
        name="indicationsIndex",
        unique=True,
    )
except:
    pass

try:
    indication_types.create_index(
        [("addressID", pymongo.ASCENDING), ("type", pymongo.ASCENDING)],
        name="indicationTypesIndex",
        unique=True,
    )
except:
    pass

try:
    indications.create_index(
        [("userID", pymongo.HASHED)],
        name="indicationUserIDIndex"
    )
except:
    pass

try:    
    indication_types.create_index(
        [("userID", pymongo.HASHED)],
        name="indicationTypesUserIDIndex"
    )
except:
    pass