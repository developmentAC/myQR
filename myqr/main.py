#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

from rich.console import Console
import typer

DATE = "7 Dec 2024"
VERSION = "v0.1.2"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

# create a Typer object to support the command-line interface
cli = typer.Typer()
console = Console()


@cli.command()
def main(bighelp: bool = False):
    """Front end of the program."""

    if bighelp:
        big_help()
        raise typer.Exit()  # end of main()

    console.print(
        "\t:dog:[bold yellow] QR code generator.\n\tStarting browser version. Use Control-C to exit from Command Line.[bold yellow]"
    )
    console.print(
        "\t:coffee:[bold green] Command: [bold yellow] Getting browser ready ..."
    )
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "myqr/myqr_streamlit.py"],
        check=False,
    )


# end of main()


def big_help():
    """Helper function -- give available command line prompts."""

    h_str = "   " + DATE + " | version: " + VERSION + " |" + AUTHOR + " | " + AUTHORMAIL
    console.print(f"[bold green] {len(h_str) * '-'}")
    console.print(f"[bold yellow]{h_str}")
    console.print(f"[bold green] {len(h_str) * '-'}")

    console.print(
        "\n\t:coffee:[bold green] Command: [bold yellow]uv run myqr"
    )


def cli_entrypoint() -> None:
    """Package entrypoint for the `myqr` console script."""
    cli()


# end of big_help()
