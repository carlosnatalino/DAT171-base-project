# make sure to run this cell before running the next one
from initial_file import validating_sum_of_squares


def tests_validating_sum_of_squares() -> None:

    test_cases = [
        (
            ["2", "x", -10, 3.3, "asd", None, "b", 4.0],
            [True, False, False, False, False, False, False, True],
        ),
        ([9, "x", -9, None], [True, False, False, False]),
    ]

    # for _in, _out in test_cases:
    #     _res = validating_sum_of_squares(_in)
    #     assert (
    #         _res == _out
    #     ), f"The function with input `{_in}` should return the value \
    # `{_out}` of type `{type(_out)}`\n but returned the value `{_res}` \
    # of type `{type(_res)}`."
