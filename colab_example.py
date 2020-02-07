

data = b'2\n0.0 0.0\n# Simple 3-component mixture\n1.0 - x[0] - x[1] >= 0.0\n'

from CitrineChallenge.python_api import analyze

results = analyze(
    input_file=data,
    n_results=1000,
    google=True
)

print(results)