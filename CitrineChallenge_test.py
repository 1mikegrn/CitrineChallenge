from CitrineChallenge.src.calculator import calculate
from os import path

def main():

    here = path.abspath(path.dirname(__file__))

    input_file, n_results = (
        path.join(here, 'tests', 'mixture.txt'),
        1000
    )

    report_values = calculate(input_file, n_results)

    return n_results, report_values.shape

def test_main():
    check1, check2 = main()
    assert check2.shape[0] == check1 + 1

if __name__ == "__main__":
    test_main()