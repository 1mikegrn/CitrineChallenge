This site is a docstring repository for the HypercubeChallenge, written by
Michael Green as a submission for the Hypercube Challenge.

Use the tabs on the left-hand side of the page to navigate to the
various document sections.

**Connect:**

Michael Green
`@Website <https://1mikegrn.github.io>`_
`@Github <https://github.com/1mikegrn>`_
`@StackOverflow <https://stackoverflow.com/users/10881573/michael-green?tab=profile>`_

Getting Started
===============

From the command prompt, the latest version this library can be installed 
via pip and git

:code:`pip install git+https://github.com/1mikegrn/HypercubeChallenge`

Where the setup file will automatically check dependencies and install
to the main module library. Once installed, calling
:code:`HyperCMD <input_file> <output_file> <n_results>` will execute the
calculation.

This library also has a colab jupyter notebook, from which calculations can be
executed without any necessary local downloads.

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/1mikegrn/HypercubeChallenge/blob/master/colab/HypercubeChallenge_notebook.ipynb

Library Structure
=================

::

    HypercubeChallenge/
        __init__.py                         # initialize CitrineChallenge
        src/                                # source module
            __init__.py                     # initialize src
            __main__.py                     # CLI access point
            calculator.py                   # main calculation module
            constraints.py                  # constraints parse point
            tools/                          # tools module
                __init__py                  # initialize tools
                cmd_reader.py               # CLI reader
                cleaning.py                 # cleaning module
                generator.py                # generator module
                saver.py                    # file output module
                quick_graphs.py             # graph generator


the built-in docstrings are all accessible via standard `?` querying in a python
shell where HypercubeChallenge is imported.