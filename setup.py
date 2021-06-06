from setuptools import setup

setup(
    name='folderstack',
    version='0.0.1',
    py_modules=['folderstack'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'folderstack = folderstack:cli',
        ],
    },
)
