from numpy import( 
    array, vstack, delete
)

from numpy.random import random_sample

from src.tools import(
    cmd_reader,
    cleaning, 
    generator,
    saver
) 

from src.constraints import Constraint

def main():

    thing, input_file, output_file, n_results = cmd_reader.reader()

    print(thing, input_file, output_file, n_results)

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

        if test_values.shape[0] == 0:
            break

        test_values = generator.generate(
            test_values=test_values,
            report_values=report_values
        )

    saver.save(report_values, output_file)

if __name__ == "__main__":
    main()