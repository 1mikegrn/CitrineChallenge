import sys

def reader():
    """
Objective: 

Interpret the inputs provided by the command-line interface (CLI). 
Though this function takes no direct inputs per se, it requires CLI inputs of
the following structure:

::

    sampler <input file> <output file> <n_results>

As such, the parameters are discussed below.

::

    :param sampler:         sampler

The console script which initiates the __main__ function in the CitrineChallenge
module.

::

    :param input_file:      str()

This parameter is a string containing the file path to the input_file. The 
input_file starts with a single line header that gives the dimensionality of the 
problem, which is defined on the unit hypercube. The next line is a single 
example feasible point. The remaining lines are a list of constraints as python 
expressions containing + , - , * , / , and ** operators. They have been 
transformed such that they all take the form g(x) >= 0.0. 

::

    :param output_file:     str()

This parameter is a string containing the file path to the output_file. The 
output_file is an empty output.txt file to which the results of the calculation
will be placed.

- if given as the argument '-b', the module will build a .txt file in the 
  directory of the input file.

::

    :param n_results:       int()

This parameter is an integer value of the number of new vector results to 
generate over the unit hypercube. 

::

    :returns:               (input_file, output_file, n_results)

Returns a tuple of the parsed CLI inputs to be utilized by the module.

    """
    assert len(sys.argv) == 4, \
        'Expected CLI input: sampler <input file> <output file> <n_results>'

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    n_results = int(float(sys.argv[3]))

    assert isinstance(input_file, str) is True, \
        'Expected <input file> value of type str()'

    assert isinstance(output_file, str) is True, \
        'Expected <output file> value of type str()'

    assert isinstance(n_results, int) is True, \
        'Expected <n_results> value of type int()'
    
    return input_file, output_file, n_results
      