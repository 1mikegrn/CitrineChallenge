
from CitrineChallenge.src.tools import(
    cmd_reader,
    saver
) 

from CitrineChallenge.src.calculator import calculate
from CitrineChallenge.src.constraints import Constraint

def main():
    """

Entry point for the command line interface. Function directs arguments from the 
CLI reader to the necessary subroutines within the library for caluclation. Once
the calculation is done, results are passed to the :code:`save()` function to be
saved.

::

    :params:    <None>

::

    :returns:   <None>
    
    """
    input_file, output_file, n_results = cmd_reader.reader()

    report_values = calculate(input_file, n_results)

    saver.save(report_values, input_file, output_file)

if __name__ == "__main__":
    main()