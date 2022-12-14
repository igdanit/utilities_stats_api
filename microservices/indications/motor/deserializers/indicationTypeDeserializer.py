
def indication_type_entity(indication_type) -> dict:
    return {
        "id": int(indication_type["_id"]),
        "userID": int(indication_type["userID"]),
        "addressID": int(indication_type["addressID"]),
        "type": indication_type["type"]
    }

def indications_type_list(indication_types):
    return [indication_type_entity(indication_type) for indication_type in indication_types]