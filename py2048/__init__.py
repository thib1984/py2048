"""
py2048 init
"""


from py2048.args import compute_args
from py2048.app import app
import colorama


def py2048():
    """
    py2048 entry point
    """
    compute_args()
    colorama.init()

    try:
        app()
    except KeyboardInterrupt:
        exit(1)