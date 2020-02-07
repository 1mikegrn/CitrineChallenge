from numpy import savetxt

def save(report_values, output_file):

    if output_file == '.':
        savetxt(r'C:\Users\1mike\desktop\output.txt', report_values)


    else:
        report_values = list(report_values)    

        with open(output_file,'w') as f: 

            f.write("\n".join(" ".join(map(str, x)) for x in report_values))