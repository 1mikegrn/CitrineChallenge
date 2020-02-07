"""
The CitrineChallenge library

This library is designed to build an array of vectors in an n-dimensional 
hypercube, whose vectors satisfy a system of non-linear constraints.

This library includes the following functions:

::

    CitrineChallenge.src.__main__.main()

this is the entry point of the command line interface. main() directs arguments
from the CLI to the necessary subroutines within the library for calculation.

::

    CitrineChallenge.src.python_api.analyze()

this is the entry point for a Python instance. analyze() takes an input argument 
of the file location for a constaints file, and an n_results integer for 
determining how many results to generate.


::

    CitrineChallenge.src.calculator.calculate(
        input_file, n_results
    )

the calculator uses the input file and n_results integer to run the calculation.
results are returned to be saved.

::

    CitrineChallenge.src.tools.cmd_reader.reader()

the reader function parses the command-line interface arguments for calculation.

::

    CitrineChallenge.src.tools.cleaning.cleaner(
        class_object, report_values, test_values
    )

the cleaning function extracts the passing test values from the test_values 
array and appends them to the report_values array, using constraints defined in
the class_object.

::

    CitrineChallenge.src.tools.generator.generate(
        test_values, report_values
    )

the generate function uses linear interpolation to build new test values from
previously rejected test values and accepted report values.

"""

from CitrineChallenge import python_api, src
