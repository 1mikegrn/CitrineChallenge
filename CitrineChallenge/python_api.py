from CitrineChallenge.src.calculator import calculate
from CitrineChallenge import python_api

def analyze(input_file, n_results):

    report_values = calculate(input_file, n_results)

    return report_values