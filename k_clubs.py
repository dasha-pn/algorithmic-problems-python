"""Task 1"""

def k_clubs(input_string: str) -> int:
    """
    Given a list of clubs and their members, determine how many students 
    followed by club information in the format
    "club_name:student_id1,student_id2,...".
    :return: The number of students who are members of exactly k clubs.
    """

    blocks = input_string.split()
    k = int(blocks[0])
    res = 0
    res_dict = {}

    for club in blocks[1:]:
        _, student_id = club.split(":")
        ids = student_id.split(",")
        for idd in ids:
            res_dict[idd] = res_dict.get(idd, 0) + 1

    for val in res_dict.values():
        if val == k:
            res += 1

    return res

def run_tests():
    """..."""

    assert k_clubs(
        "2 robotics:1,2,3 chess:2,4,5 drama:1,2,6"
    ) == 1

    assert k_clubs(
        "1 chess:10,20,30"
    ) == 3

    assert k_clubs(
        "3 chess:1,2 drama:2,3"
    ) == 0

    assert k_clubs(
        "2 music:1,2 sport:1,3"
    ) == 1

    # assert k_clubs(
    #     "1 robotics:1,2 empty: chess:3"
    # ) == 3

    # assert k_clubs(
    #     "1 robotics:1, 2, ,3"
    # ) == 3

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
