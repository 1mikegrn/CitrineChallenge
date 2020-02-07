from numpy import array
from numpy.random import random_sample

from CitrineChallenge.src.tools import(
    cleaning, 
    generator
)

from CitrineChallenge.src.constraints import Constraint

def calculate(input_file, n_results):
    """
Objective:

Generate an array of vectors which satisfy the constraints, input by the 
provided constraints input_file. Delegates the calculation between the clean()
and generate() functions until all the results generated satisfy all 
constraints. 

::

    :param input_file:      str()

string which points to the constraints file from outside the module. input_file 
is parsed by the Constratints() class so to generate the constraints parameter,
the hypercube dimensionality, and the example point.

::

    :param n_results:       int()

n_results is the integer_value of results to be generated.

::

    :return:                report_values

report_values is the NxM array of results determined to satisfy the constraints,
where N is the n_results + 1 and M is the hypercube dimensionality.
    
    """
    # build the contraint class object from provided input file
    class_object = Constraint(input_file)

    # extract hypercube dimensionality and example point from the class_object
    example = class_object.get_example()
    n_dim = class_object.get_ndim()

    # generate random sample in hypercube
    test_values = random_sample((n_results, n_dim))

    #initialize the report_values array with the given example point
    report_values = array([example])

    while test_values.shape[0] > 0:

        # clean test values according to constraints in class_object
        test_values, report_values = cleaning.clean(
            class_object=class_object,
            test_values=test_values,
            report_values=report_values
        )

        # calculation is done if test_values is empty
        if test_values.shape[0] == 0:
            break

        # generate new test values by replacing rejected values
        test_values = generator.generate(
            test_values=test_values,
            report_values=report_values
        )

    # return accepted values when done
    return report_values
