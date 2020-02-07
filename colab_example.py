

data = b'2\n0.0 0.0\n# Simple 3-component mixture\n1.0 - x[0] - x[1] >= 0.0\n'

lines = [x for x in data.decode().split('\n') if x != '']

from CitrineChallenge.python_api import analyze

results = analyze(
    input_file=lines,
    n_results=1000,
    google=True
)

print(results)