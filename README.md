# MyQR: An Interactive QR Code Generator

- Oliver Bonham-Carter, [Web](https://www.oliverbonhamcarter.com/)
- email: obonhamcarter@allegheny.edu
- Date: 19 April 2026

---

![logo](graphics/myQrCode.png)

---

## Table of contents
- [MyQR: An Interactive QR Code Generator](#myqr-an-interactive-qr-code-generator)
  - [Table of contents](#table-of-contents)
    - [Command Summary](#command-summary)
    - [Creating QRcodes With Browser Tool](#creating-qrcodes-with-browser-tool)
  - [A work in progress](#a-work-in-progress)

### Command Summary

* The project uses [uv](https://docs.astral.sh/uv/) and the [Streamlit](https://docs.streamlit.io/) and [qrcode](https://pypi.org/project/qrcode/) libraries.
* Use the following command from the project root (the directory containing `pyproject.toml`) to create/sync the environment and install dependencies.

`uv sync`

Below are commands to run MyQR using the UV-managed virtual environment.

- Basic help to run the project

``` bash
uv run myqr --help
```
- Involved help to run the project

``` bash
uv run myqr --bighelp
```

- Actual command to engage the program

``` bash
uv run myqr
```

- Run tests

``` bash
uv run pytest
```

### Creating QRcodes With Browser Tool

![logo](graphics/panel.png)

- Enter the text to encode in a QR code
- Pick your colours
- Select size and boarder width of the qr `.png` file
- Select the `Generate QR Code` button.
- View the QRcode as a `.png` image that will appear.
- Check the output directory: `0_out/` for your `.png` file, or save it by right-clicking on the image itself.

## A work in progress

Check back often to see the evolution of the project!! If you would like to contribute to this project, __then please do!__ For instance, if you see some low-hanging fruit or task that you could easily complete, that could add value to the project, then I would love to have your insight.

Otherwise, please create an Issue for bugs or errors. Since I am a teaching faculty member at Allegheny College, I may not have all the time necessary to quickly fix the bugs and so I would be very happy to have any help that I can get from the OpenSource community for any technological insight. Much thanks in advance. I hope that this project helps you find the knowledge from PubMed that you require for your project. :-)
