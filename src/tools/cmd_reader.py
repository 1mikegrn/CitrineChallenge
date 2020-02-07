import sys

def reader():
    """
Objective:
    
    """
    assert len(sys.argv) == 4, \
        'Expected CLI input <sampler> <input file> <output file> <n_results>'

    thing = sys.argv[0]
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    n_results = int(float(sys.argv[3]))

    assert isinstance(input_file, str) is True, \
        'Expected <input file> value of type str()'

    assert isinstance(output_file, str) is True, \
        'Expected <output file> value of type str()'

    assert isinstance(n_results, int) is True, \
        'Expected <n_results> value of type int()'
    
    return thing, input_file, output_file, n_results
      