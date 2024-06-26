"""
pygitscrum argparse gestion
"""

import argparse
import sys



class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ", ".join(action.option_strings) + " " + args_string

    def _format_args(self, action, default_metavar):
        get_metavar = self._metavar_formatter(action, default_metavar)
        if action.nargs == argparse.ONE_OR_MORE:
            return "%s" % get_metavar(1)
        else:
            return super(CustomHelpFormatter, self)._format_args(
                action, default_metavar
            )


def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="py2048 game",
        epilog="""
        Full documentation at: <https://github.com/thib1984/py2048>.
        Report bugs to <https://github.com/thib1984/py2048/issues>.
        MIT Licence.
        Copyright (c) 2024 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
        formatter_class=CustomHelpFormatter,
    )
    my_group = my_parser.add_mutually_exclusive_group()
    my_group.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="mise à jour de py2048",
    )

    args = my_parser.parse_args()
    return args
