# HypercubeChallenge

[![Build Status](https://travis-ci.com/1mikegrn/HypercubeChallenge.svg?branch=master)](https://travis-ci.com/1mikegrn/HypercubeChallenge)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/1mikegrn/HypercubeChallenge/blob/master/colab/HypercubeChallenge_notebook.ipynb)
[![DocSite](https://img.shields.io/badge/Docs-Site-blue)](https://1mikegrn.github.io/HypercubeChallenge/)

HypercubeChallenge is the Python library built by Michael Green as a submission
for the Hypercube Challenge.

## Objective

build an array of vectors in an n-dimensional hypercube, whose vectors
satisfy a system of non-linear constraints.

## Solution

The current method is an iterative process which, from a set of random
vectors within the hypercube, linearly interpolates between good vectors and bad
vectors to generate new vectors, until the number of required accepted vectors
is reached. An initial set of random vectors is generated as an array called
test_values. test_values is then passed through a cleaning function to extract
vectors which satisfy the constraints provided, and place these vectors in a
separate array called report_values to be reported.

Now that we have two arrays, the arrays are passed through a generator function.
For each vector in the test_values array, the generator function pairs this
vector with a random vector from the report_values array. Linear interpolation
is then used to replace the vector in the test_values array with a new vector
which is between the good vector and bad vector. These new vectors are then
passed back to the cleaning function for evaluation. This process of cleaning
and generating is repeated until there are no bad vectors.

## Getting Started

From the command prompt, the latest version this library can be installed
via pip and git

    pip install git+https://github.com/1mikegrn/HypercubeChallenge

Where the setup file will automatically check dependencies and install
to the main module library. Once installed, calling `HyperCMD
<input_file> <output_file> <n_results>` will execute the calculation from the
command line.

This library also has a colab jupyter notebook, from which calculations can be
executed without any necessary local downloads. See the included repo-badge at
the top of this page to be directed there.
