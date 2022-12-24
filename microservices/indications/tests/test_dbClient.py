import pytest
from motorService.motorClient import IndicationMongoService
from config import settings

async def test_async_motor_indication():
    with IndicationMongoService(uri=settings.TEST_DATABASE_URL) as client:

        # TEST CONNECTION TO INDICATIONS COLLECTION
        entry_list = await client.get_indications({
            "indication": 1
        }, 1)
        entry = entry_list[0]
        assert all((
            entry['indication'] == 1,
            entry["indicationTypeID"] == 1,
            entry['createdAt'] == {
                "day": 1,
                "month": 1,
                "year": 1970,
            }
        ))

        # TEST INDICATION TYPES COLLECTION
        entry_list = await client.get_indication_types({
            "addressID": 1
        }, 1)
        entry = entry_list[0]
        assert all((
            entry["addressID"] == 1,
            entry["type"] == 'ABOBUS',
        ))
