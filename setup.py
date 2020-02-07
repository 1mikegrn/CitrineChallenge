from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CitrineChallenge',
    version='0.0.1',
    description='Citrine Informatics Challenge - Scientific Software Engineer',
    long_description=long_description,
    url='https://github.com/1mikegrn/CitrineChallenge',
    author='Michael Green',
    author_email='1mikegrn@gmail.com',
    license='GPL-3.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: STEM research',
        'License :: OSI Approved :: GPL-3.0 License',
    ],

    packages=find_packages(),

    package_data={
    },

    include_package_data=False,

    python_requires='>=3.6',

    install_requires=[
        'numpy',
        'matplotlib'
    ],

    entry_points={
        'console_scripts': ['sampler=CitrineChallenge.src.__main__:main']
    },

    project_urls={
        'GitHub': 'https://github.com/1mikegrn/CitrineChallenge/',
        'DocSite': 'https://1mikegrn.github.io/CitrineChallenge/',
        'Personal Blog': 'https://1mikegrn.github.io',
        'Google Scholar': 'https://scholar.google.com/citations?user=DxFljRYAAAAJ&hl=en'
    }
)