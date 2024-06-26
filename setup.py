from setuptools import setup

setup(
    name="py2048",
    version="0.1.0",
    description="py2048 game in terminam",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/py2048#readme",
    url="https://github.com/thib1984/py2048",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    packages=["py2048"],
    install_requires=["columnar","termcolor", "colorama"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "py2048=py2048.__init__:py2048"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
