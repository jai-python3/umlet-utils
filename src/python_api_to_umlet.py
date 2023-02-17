# -*- coding: utf-8 -*-
import logging
import os
import pathlib
import sys
from datetime import datetime
from pathlib import Path

import click
from colorama import Fore, Style

from umlet.python_to_umlet.converter import Converter

TIMESTAMP = str(datetime.today().strftime("%Y-%m-%d-%H%M%S"))

DEFAULT_OUTDIR = os.path.join(
    "/tmp/",
    os.path.splitext(os.path.basename(__file__))[0],
    TIMESTAMP,
)


LOGGING_FORMAT = "%(levelname)s : %(asctime)s : %(pathname)s : %(lineno)d : %(message)s"

LOG_LEVEL = logging.INFO

DEFAULT_VERBOSE = False


def print_green(msg: str = None) -> None:
    """Print message to STDOUT in yellow text.

    :param msg: {str} - the message to be printed
    """
    if msg is None:
        raise Exception("msg was not defined")

    print(Fore.GREEN + msg + Style.RESET_ALL)


def print_yellow(msg: str = None) -> None:
    """Print message to STDOUT in yellow text.

    :param msg: {str} - the message to be printed
    """
    if msg is None:
        raise Exception("msg was not defined")

    print(Fore.YELLOW + msg + Style.RESET_ALL)


@click.command()
@click.option("--indir", help="The directory contain Python .py class files")
@click.option("--logfile", help="The log file")
@click.option(
    "--outdir",
    help=f"The default is the current working directory - default is '{DEFAULT_OUTDIR}'",
)
@click.option("--outfile", help="The output final report file")
@click.option(
    "--verbose",
    is_flag=True,
    help=f"Will print more info to STDOUT - default is '{DEFAULT_VERBOSE}'",
)
def main(indir: str, logfile: str, outdir: str, outfile: str, verbose: bool):
    """Get table counts from Redshift."""

    error_ctr = 0

    if error_ctr > 0:
        sys.exit(1)

    if indir is None:
        indir = os.path.abspath(os.getcwd())
        print_yellow(
            f"--indir was not specified and therefore was set to default '{indir}'"
        )

    if outdir is None:
        outdir = DEFAULT_OUTDIR
        print_yellow(f"--outdir was not specified and therefore was set to '{outdir}'")

    if not os.path.exists(outdir):
        pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
        print_yellow(f"Created output directory '{outdir}'")

    if outfile is None:
        outfile = os.path.join(
            outdir, os.path.splitext(os.path.basename(__file__))[0] + ".uxf"
        )
        print_yellow(
            f"--outfile was not specified and therefore was set to '{outfile}'"
        )

    if logfile is None:
        logfile = os.path.join(
            outdir, os.path.splitext(os.path.basename(__file__))[0] + ".log"
        )
        print_yellow(
            f"--logfile was not specified and therefore was set to '{logfile}'"
        )

    logging.basicConfig(filename=logfile, format=LOGGING_FORMAT, level=LOG_LEVEL)

    classes_only_outfile = outfile
    outfile = outfile.replace(".uxf", f"_{TIMESTAMP}.uxf")
    classes_only_outfile = classes_only_outfile.replace(
        ".uxf", f"_classes_only_{TIMESTAMP}.uxf"
    )

    converter = Converter(
        indir=indir,
        outdir=outdir,
        outfile=outfile,
        classes_only_outfile=classes_only_outfile,
        logfile=logfile,
        verbose=verbose,
    )

    converter.run()

    print(f"The log file is '{logfile}'")
    print_green(f"Execution of {os.path.abspath(__file__)} completed")


if __name__ == "__main__":
    main()
