"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mrst2text` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``rst2text.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``rst2text.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
from .document import RstDocument


@click.command()
@click.argument("names", nargs=-1)
def main(names):
    click.echo(repr(names))
    print('args', names[0])

    doc = RstDocument(names[0])
    # print(doc.rst)
    # print(doc.myrst)
    # with open("output.txt", "w+") as outf:
    #     outf.write(doc.myrst["whole"])

    print('whole===============')
    # print(type(doc.myrst["whole"]))
