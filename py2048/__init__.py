"""
py2048 init
"""


from py2048.args import compute_args
from py2048.app import app
from py2048.update import update
import colorama


def py2048():
    """
    py2048 entry point
    """
    
    colorama.init()

    try:
        if compute_args().update:
            update()
        else:
            app()
    except KeyboardInterrupt:
        exit(1)