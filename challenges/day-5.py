"""
Create acronyms

Difficulty: Medium

Question: Given a string with words separated by spaces, create an acronym by taking the first letter of each word. The output string should be in upper case.

Examples:

Test Case 1:
Input - 'Laboratory for Physicists'
Output - 'LFP'
Explanation - First letter of 'laboratory' is L. First letter of 'for' is F. For 'Physicists' it's P. So our acronym becomes LFP.

Test Case 2:
Input - 'State Bank of India'
Output - 'SBOI'
Explanation - First letter of 'state' is S. For Bank it's B, for 'of' it's O, for India it's I. So our acronym becomes SBOI.
"""


def create_acronym(input_string: str) -> str:
    return "".join(map(lambda x: x[0].upper(), input_string.split()))


def test_1():
    assert create_acronym("Laboratory for Physicists") == "LFP"


def test_2():
    assert create_acronym("State Bank of India") == "SBOI"


def test_3():
    assert create_acronym("  Laboratory \tfor \tPhysicists  ") == "LFP"


def test_4():
    assert create_acronym("    ") == ""


def test_5():
    assert create_acronym("SLB") == "S"


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
