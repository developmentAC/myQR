#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rich.console import Console
import typer
import os

DATE = "7 Dec 2024"
VERSION = "v0.1.2"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"

# create a Typer object to support the command-line interface
cli = typer.Typer()
console = Console()


@cli.command()
def main(client: str = "", bighelp: bool = False):
    """Front end of the program."""

    if client.lower() == "qr":

        console.print(
            "\t:dog:[bold yellow] QR code generator.\n\tStarting browser version. Use Control-C to exit from Command Line.[bold yellow]"
        )
        console.print(
            f"\t:coffee:[bold green] Command: [bold yellow] Getting browser ready ..."
        )
        os.system("poetry run streamlit run myqr/myqr_streamlit.py")

    elif bighelp:
        bigHelp()
        exit()  # end of main()


# end of main()


def bigHelp():
    """Helper function -- give available command line prompts."""

    h_str = "   " + DATE + " | version: " + VERSION + " |" + AUTHOR + " | " + AUTHORMAIL
    console.print(f"[bold green] {len(h_str) * '-'}")
    console.print(f"[bold yellow]{h_str}")
    console.print(f"[bold green] {len(h_str) * '-'}")

    console.print(
        f"\n\t:coffee:[bold green] Command: [bold yellow]poetry run myqr --client qr"
    )


# end of bigHelp()
