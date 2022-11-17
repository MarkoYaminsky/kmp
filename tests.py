import time
from kmp import knuth_morris_pratt


def kmp_with_time(string: str, substring: str, test_index: int):
    start = time.time()
    result = knuth_morris_pratt(string, substring)
    end = time.time()
    print(f'Test number {test_index} evaluated the result in {end - start} second(s)')
    return result


def run_tests(cases: list[dict]):
    for test_number, test in enumerate(cases):
        string = cases[test_number]['string']
        substring = cases[test_number]['substring']
        result = cases[test_number]['result']
        assert kmp_with_time(string, substring, test_number + 1) is result


if __name__ == '__main__':
    test_cases = [
        # best case scenarios

        # 1 (instant match)
        {
            'string': 'Sviatoslav kytsia',
            'substring': 'Svi',
            'result': True
        },
        # 2 (no matching characters at all)
        {
            'string': '123123',
            'substring': 'Vitalik',
            'result': False
        },

        # average case scenarios

        # 3
        {
            'string': 'Some text lorem ipsum dolor sit amet',
            'substring': 'ipsum',
            'result': True
        },
        # 4
        {
            'string': '123 456 789 063 499 293 310',
            'substring': '99 ',
            'result': True
        },

        # worst case scenarios - a lot of partly matches with substring

        # 6
        {
            'string': 'I lo I lov I lovw I lovs I los I l I I I love',
            'substring': 'I love',
            'result': True
        },
        # 7
        {
            'string': '1111111111111111111111111111118',
            'substring': '1111111117',
            'result': False
        },
    ]

    run_tests(test_cases)
