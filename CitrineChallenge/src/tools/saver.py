from numpy import savetxt
from os.path import split 

def save(report_values, input_file, output_file):

    if output_file == '-b':

        file_output = split(input_file)[0] + 'output.txt'

        savetxt(file_output, report_values)


    else:
        
        report_values = list(report_values)    

        with open(output_file,'w') as f: 

            f.write("\n".join(" ".join(map(str, x)) for x in report_values))