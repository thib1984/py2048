"""
--update scripts
"""

import subprocess
from shutil import which


def update():
    """
    entry point for --update
    """
    prog = "pip3"
    if (which("pip3")) is None:
        prog = "pip"
    params = [
        prog,
        "install",
        "--upgrade",
        "py2048",
    ]
    subprocess.check_call(params)
