from CitrineChallenge.src.calculator import calculate

def analyze(input_file, n_results):

    """Provides colab entry point for calculation"""

    report_values = calculate(input_file, n_results)

    return report_values
