def validate_user_data(data):
    required_fields = ['name', 'preferences', 'dietary_restrictions']
    for field in required_fields:
        if field not in data:
            return False, f"{field} is missing"
    return True, None
