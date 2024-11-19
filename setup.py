from setuptools import setup, find_packages

setup(
    name='P2P_CKKS',
    description='Python implementations of P2P CKKS',
    author='Elvis Antwi Sarfo',
    author_email='',
    license='',
    install_requires=[
        'sympy',
        'pytest',
    ],
    packages=['ckks', 'tests', 'util']
)