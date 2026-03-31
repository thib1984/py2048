from setuptools import setup

setup(
    name="pyterm2048",
    version="0.1.2",
    description="pyterm2048 game in terminal",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/pyterm2048#readme",
    url="https://github.com/thib1984/pyterm2048",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    license_files="LICENSE.txt",
    packages=["pyterm2048"],
    install_requires=["columnar","termcolor", "colorama"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pyterm2048=pyterm2048.__init__:pyterm2048"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
