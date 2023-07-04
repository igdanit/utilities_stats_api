# SHOULD LAUNCH ONLY FOR EMPTY DATABASE.
# Create collections needed for project and indexes for them.
import sys

sys.path.append("..")

import pymongo
from indications.config import settings

client = pymongo.MongoClient(settings.TEST_DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]
indications = db.get_collection("indications")
indication_types = db.get_collection("indicationTypes")

indications.create_index(
    [("createdAt", pymongo.DESCENDING), ("indicationTypeID", pymongo.ASCENDING)],
    name="indicationsIndex",
    unique=True,
)

indication_types.create_index(
    [("addressID", pymongo.ASCENDING), ("type", pymongo.TEXT)],
    name="indicationTypesIndex",
    unique=True,
)

indication_types.insert_one({"addressID": 1, "type": "ABOBUS"})


indications.insert_one(
    {
        "indication": 1,
        # Fetch first entry with addressID=1 and convert ObjectID to hex string
        "indicationTypeID": str(indication_types.find_one({"addressID": 1})["_id"]),
        "createdAt": {"day": 1, "month": 1, "year": 1970},
    }
)
