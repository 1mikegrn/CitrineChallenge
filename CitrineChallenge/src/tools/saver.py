from numpy import savetxt
from os.path import split 

def save(report_values, input_file, output_file):
    """
Objective:

Save the generated data file on the local machine as specified by the
output_file.

::

    :param report_values:       <numpy.array>

array of vectors to be exported.

::

    :param input_file:          str()

input file string for if an output file is to be generated.

::

    :param output_file:         str()

local .txt file for the results to be written to.

::

    :return:                    <None>

    """
    if output_file == '-b':

        file_output = split(input_file)[0] + 'output.txt'

        savetxt(file_output, report_values)


    else:
        
        report_values = list(report_values)    

        with open(output_file,'w') as f: 

            f.write("\n".join(" ".join(map(str, x)) for x in report_values))