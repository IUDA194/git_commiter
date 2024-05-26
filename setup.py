from setuptools import setup, find_packages

setup(
    name='gitc',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gitc=main:main',
        ],
    },
)