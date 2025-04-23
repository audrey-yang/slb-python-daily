"""
Trace violations

Difficulty: Medium

Question: Do you know about relational databases? They are the huge pools of data that store data in an efficient way for performing Create, Read, Update and Delete (CRUD) operations on data. To facilitate this, they employ many techniques - one of them being to store each set of unique data with a unique identifier, called primary key. There are other constraints that can be used as keys as well - for example in a customer database, customer email can be kept as a key besides the primary key, given that every customer email should be unique. In this case, it's called a candidate key. Here, you are the esteemed Database Administrator (DBA), and your task is to deduplicate the data. Data deduplication refers to the process of eliminating already existing duplicate data or preventing duplicate data from entering the database. But real-world data is messy, containing lots of duplicates. Here, you are given incoming employee data that consists of their name, address, employee email, phone number, etc. Your job is to create a filter that removes incoming duplicates from the database you are given. The incoming data is in the form of a list of tuples (DATA_KEY, NAME, EMAIL, ADDRESS, PHONE) The following constraints are given: DATA_KEY, EMPLOYEE_EMAIL and PHONE are the keys - that is, they should be unique. Complete the function db_trace_violations(data) so that it takes in incoming data as a list of tuples and returns a list of indexes of the elements overwritten.

Input Format: list of tuples
Output Format: list of integers

Examples:
Test Case 1:
Input: [(1, "A", "a@b.com", "23, Lake Avenue", "919734536286"), (1, "B", "a@b.com", "23, Bard Colony", "919734536286"), (2, "B", "b@c.com", "23, Shakespeare Colony", "919749271189")]
Output: [1]
Explanation: As you move through the data, you see that the element at index 1, ie., the second element, violated multiple constraints, so you log it. At the end of the loop, since there are no other duplicates, you return the list containing only one element. NOTE THAT the second element is not compared with the third element because it wasn't stored.
"""


def db_trace_violations(data: list[tuple[int, str, str, str, str]]) -> list[int]:
    """
    Function to process data as a list of tuples and find indices of elements violating unique constraints.

    Args:
        data (list[tuple]): List of tuples containing employee data
    Returns:
        list[int]: List of indices of elements that were overwritten due to duplicates
    """
    keys, emails, phone_numbers = set(), set(), set()
    violations_list = []

    for i, entry in enumerate(data):
        (data_key, _, email, _, phone_number) = entry
        if data_key in keys or email in emails or phone_number in phone_numbers:
            violations_list.append(i)
        else:
            keys.add(data_key)
            emails.add(email)
            phone_numbers.add(phone_number)

    return violations_list


def test_1():
    data = [
        (1, "A", "a@b.com", "23, Lake Avenue", "919734536286"),
        (1, "B", "a@b.com",
         "23, Bard Colony", "919734536286"),
        (2, "B", "b@c.com", "23, Shakespeare Colony", "919749271189")
    ]
    assert db_trace_violations(data) == [1]


def test_2():
    data = []
    assert db_trace_violations(data) == []


def test_3():
    data = [(1, "A", "a@b.com", "23, Lake Avenue", "919734536286")]
    assert db_trace_violations(data) == []


def test_3():
    # Duplicate picked up already won't count
    data = [
        (1, "A", "a@b.com", "23, Lake Avenue", "919734536286"),
        (1, "B", "b@c.com",
         "23, Bard Colony", "919734536286"),
        (2, "B", "b@c.com", "23, Shakespeare Colony", "919749271189")
    ]
    assert db_trace_violations(data) == [1]


def test_4():
    # Multiple violations on phone number
    data = [
        (1, "A", "a@b.com", "23, Lake Avenue", "919734536286"),
        (2, "B", "b@b.com", "23, Lake Avenue", "919734536286"),
        (3, "C", "c@b.com", "23, Lake Avenue", "919734536286"),
    ]
    assert db_trace_violations(data) == [1, 2]


def test_5():
    # Multiple with no violations
    data = [
        (1, "A", "a@b.com", "23, Lake Avenue", "919734536286"),
        (2, "A", "b@b.com", "23, Lake Avenue", "919734536287"),
        (3, "A", "c@b.com", "23, Lake Avenue", "919734536288"),
    ]
    assert db_trace_violations(data) == []


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("All tests passed.")
