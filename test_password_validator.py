from password_validator import is_valid_password


#1 Accepts an exactly 8-character password meeting the requirements.
def test_password_with_exactly_8_characters_is_valid():
	assert is_valid_password("Abcdef12") is True


# Accepts a longer password meeting the requirements.
def test_password_with_more_than_8_characters_is_valid():
	assert is_valid_password("Password123") is True


#3 Rejects a password shorter than 8 characters.
def test_password_with_7_characters_is_invalid():
	assert is_valid_password("Abcde12") is False


#4 Rejects a password without a number.
def test_password_without_number_is_invalid():
	assert is_valid_password("Abcdefgh") is False


# Rejects a password without an uppercase letter.
def test_password_without_uppercase_letter_is_invalid():
	assert is_valid_password("abcdefg1") is False


#6 Rejects a password containing numbers only.
def test_password_with_numbers_only_is_invalid():
	assert is_valid_password("12345678") is False


#7 Rejects an empty password.
def test_empty_password_is_invalid():
	assert is_valid_password("") is False
#8 Rejects a password that contains a space.

def test_password_with_space_is_invalid():
    assert is_valid_password("Abcdef 12") is False
  # python -m pytest -v
  
def test_password_with_special_character_is_valid():
	assert is_valid_password("Abcdef!2") is True