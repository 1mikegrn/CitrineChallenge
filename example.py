from HypercubeChallenge.src.tools import(
    saver
)

from HypercubeChallenge.src.calculator import calculate
from HypercubeChallenge.src.constraints import Constraint

from os import path

here = path.abspath(path.dirname(__file__))

def main():

    input_file, output_file, n_results = (
        path.join(here, 'tests', 'alloy.txt'),
        path.join(here, 'output.txt'),
        1000
    )

    report_values = calculate(input_file, n_results)

    saver.save(report_values, input_file, output_file)


if __name__ == "__main__":
    main()