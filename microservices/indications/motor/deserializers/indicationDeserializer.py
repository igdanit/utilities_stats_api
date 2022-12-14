
def indicationEntity(indication) -> dict:
    return {
        "id": int(indication["_id"]),
        "indication": int(indication["indication"]),
        "indication_type_id": int(indication["indication_type"]),
        "created_at": indication["created_at"]
    }

def indicationResponseEntity(indication) -> dict:
    return {
        "id": int(indication["_id"]),
        "indication": int(indication["indication"]),
        "created_at": indication["created_at"]
    }

def indicationResponseListEntity(indications) -> list:
    return [indicationResponseEntity(indication) for indication in indications]