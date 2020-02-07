from numpy import( 
    array, vstack, delete
)

from numpy.random import random_sample

from src.tools import(
    cmd_reader,
    cleaning, generator
) 
from src.constraints import Constraint

def main():

    input_file, output_file, n_results = (
        r"D:\Programming\CitrineChallenge\tests\alloy.txt",
        r'D:\Programming\CitrineChallenge\output.txt',
        1000
    )

    class_object = Constraint(input_file)

    example = class_object.get_example()

    n_dim = class_object.get_ndim()

    test_values = random_sample((n_results, n_dim))

    report_values = array([example])

    while test_values.shape[0] > 0:

        test_values, report_values = cleaning.clean(
            class_object=class_object,
            test_values=test_values,
            report_values=report_values
        )

        test_values = generator.generate(
            test_values=test_values,
            report_values=report_values
        )

    print(report_values.shape)

if __name__ == "__main__":
    main()