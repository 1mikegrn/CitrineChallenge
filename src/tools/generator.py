from numpy import array

from numpy.random import randint, random_sample

def generate(test_values, report_values):

    new_values = list()
    
    for i in range(test_values.shape[0]):

        try:
            choice = randint(report_values.shape[0]-1)
        except:
            choice = 0
        
        new_values.append(switch(
            report_values[choice,:], 
            test_values[i, :]
        ))

    test_values = array(new_values)

    return test_values, report_values


def switch(good, bad):

    pct = random_sample()
    new_point = (1-pct)*good + pct*bad

    return new_point
