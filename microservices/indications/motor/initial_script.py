# SHOULD LAUNCH ONLY FOR EMPTY DATABASE.
# Create collections needed for project and indexes for them.
import sys

sys.path.append("..")

import pymongo
from src import settings

client = pymongo.MongoClient(settings.DATABASE_URL)

db = client[settings.MONGO_INITDB_DATABASE]
indications = db.indications
indications_types = db.indicationsTypes

indications.create_index(
    [
        ('createdAt', pymongo.DESCENDING),
        ('indicationTypeID', pymongo.ASCENDING)
    ],
    name = 'indicationsIndex',
    unique = True
)

indications_types.create_index(
    [
        ('addressID', pymongo.ASCENDING),
        ('type', pymongo.TEXT)
    ],
    name = 'indicationsTypesIndex',
    unique = True
)


