# Write a Python function that checks if a password is valid.
# A valid password must be at least 8 characters, contain at least
# one number, and at least one uppercase letter.
def is_valid_password(password: str) -> bool:
	return (
		len(password) >= 8
		and any(character.isdigit() for character in password)
		and any(character.isupper() for character in password)
	)