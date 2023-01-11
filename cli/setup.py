from setuptools import setup, find_packages

setup(
    name='goodmorning',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    requires=[
        "Click"
    ],
    entry_points={
        "console_scripts": [
            "goodmorning = goodmorning:say_goodmorning"
        ]
    }
)