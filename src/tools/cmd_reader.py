import sys

def cmd_reader():

    assert len(sys.argv) == 4, \
        'Expected CLI input <input file> <output file> <n_results>'

    assert isinstance(sys.argv[1], str) is True, \
        'Expected <input file> value of type str()'

    assert isinstance(sys.argv[2], str) is True, \
        'Expected <output file> value of type str()'

    assert isinstance(sys.argv[3], int) is True, \
        'Expected <n_results> value of type int()'

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    n_results = sys.argv[3]
    
    return input_file, output_file, n_results
      