from setuptools import setup

setup(
    name='yardb',
    version='0.1.0',
    packages=['yardb'],
    entry_points={
        'console_scripts': [
            'yardb = yardb.__main__:main'
        ]
    }
)