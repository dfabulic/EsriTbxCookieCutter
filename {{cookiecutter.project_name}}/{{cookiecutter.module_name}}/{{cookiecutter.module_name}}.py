"""
@author: {{cookiecutter.author}}
@contact: {{cookiecutter.email}}
@version: {{cookiecutter.release}}
@description: {{cookiecutter.short_description}}
@requirements:
@copyright: {{cookiecutter.copyright}}, {{cookiecutter.year}}
"""
import argparse


def {{cookiecutter.method_name}}(arg1=None, arg2=None):
    """<Function description>

    Keyword arguments:
        arg1 -- ...
        arg2 -- ...
    """
    print("Done.")


if __name__ == "__main__":

    # ArgumentParser will automatically create usage message if script is
    # invoked with no or invalid parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("positional_argument", help="Example of required positional argument")
    parser.add_argument("-a","--argument", type=str, help="Example of optional keyword argument")

    args = parser.parse_args()

    {{cookiecutter.method_name}}(
            arg1=args.positional_argument,
            arg2=args.argument
    )
