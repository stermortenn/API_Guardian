def validate_response(expected_status, actual_status, expected_body, actual_body):
    if expected_status != actual_status:
        return False

    if expected_body:
        for key, value in expected_body.items():
            if actual_body.get(key) != value:
                return False

    return True