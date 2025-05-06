"""
Aadhaar Validation

Difficulty: Easy

A user enters their Aadhaar number in a field. Your task is to check if it contains exactly 12 digits or not. And, whether it is completely numeric or not. If it isn't 12 digits long, raise an exception with the message 'Please enter exactly 12 digits'. If it contains anything other than numbers, raise an exception with the message 'Please enter numbers only'.

Examples:

Test Case 1:
Input - 111122223333
Output - valid
Explanation - Both the conditions are met.

Test Case 2:
Input - 1234abcd1234
Output - Please enter numbers only
Explanation - Input contains alphabets.
"""


class AadhaarLengthError(Exception):
    """Custom exception class for length errors"""
    pass


class AadhaarInputError(Exception):
    """Custom exception class for input errors, i.e. containers non-numeric characters"""
    pass


def validate(number: str) -> bool:
    """
    Checks if the input is a valid Aadhaar number

    Args:
        number: Aadhaar number as a string

    Returns:
        bool: whether the input is valid as an Aadhaar number

    Throws:
        AadhaarLengthError if number has more or less than 12 characters
        AadhaarInputError if number has non-numeric characters
    """
    if len(number) != 12:
        raise AadhaarLengthError("Please enter exactly 12 digits")

    if not number.isnumeric():
        raise AadhaarInputError("Please enter numbers only")

    return True


def test_good():
    assert validate("111122223333") is True


def test_num_len_under():
    exception_was_thrown = False
    try:
        validate("1")
    except AadhaarLengthError as e:
        exception_was_thrown = True
        assert e.args[0] == "Please enter exactly 12 digits"
    assert exception_was_thrown is True


def test_num_len_over():
    exception_was_thrown = False
    try:
        validate("11112222333345678")
    except AadhaarLengthError as e:
        exception_was_thrown = True
        assert e.args[0] == "Please enter exactly 12 digits"
    assert exception_was_thrown is True


def test_alpha():
    exception_was_thrown = False
    try:
        validate("1234abcd1234")
    except AadhaarInputError as e:
        exception_was_thrown = True
        assert e.args[0] == "Please enter numbers only"
    assert exception_was_thrown is True


def test_alpha_len_off():
    exception_was_thrown = False
    try:
        validate("1234abcd1234abcde")
    except AadhaarLengthError as e:
        exception_was_thrown = True
        assert e.args[0] == "Please enter exactly 12 digits"
    assert exception_was_thrown is True


if __name__ == "__main__":
    test_good()
    test_num_len_under()
    test_num_len_over()
    test_alpha()
    test_alpha_len_off()
    print("All tests passed.")
