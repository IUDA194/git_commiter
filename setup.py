from setuptools import setup, find_packages

setup(
    name='gc',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gitc=main:main',
        ],
    },
)