from CitrineChallenge.src.calculator import calculate

def analyze(input_file, n_results, **kwargs):

    """Provides colab entry point for calculation"""

    report_values = calculate(
        input_file,
        n_results,
        **kwargs
    )

    return report_values
