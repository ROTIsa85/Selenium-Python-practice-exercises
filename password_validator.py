def is_valid_password(password):
    has_length = len(password) >= 8
    has_number = any(ch.isdigit() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_no_space = " " not in password
    
    return has_length and has_number and has_upper and has_no_space