import streamlit as st
import qrcode
import os
import io
from PIL import Image

# import local files
from myqr import (
    fileOps as fo,
)  # input local file to assist with file operations

OUTPUTDIR = "0_out/"

# Oliver Bonham-Carter
# obonhamcarter@allegheny.edu
# Date: 7th Dec 2024


def generate_qrcode(data, color, bgcolor, box_size, border, fname):
    """Function to generate QR code with customization"""

    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)

    # Adding data to the instance 'qr'
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=bgcolor)  # "#23dda0"

    savedFile = saveFile(bgcolor, color, fname, img, qr)

    #### view png file

    if savedFile is not None:
        # Open and display the PNG image
        image = Image.open(savedFile)
        # st.image(image, caption="Uploaded PNG", use_column_width=True)
        st.image(image, caption="Uploaded PNG", use_container_width=True)


# end of generate_qrcode()


def saveFile(bgcolor, color, fname: str, img, qr) -> None:
    """Function to save the image to a file. Check whether filename exists before saving."""
    img = qr.make_image(fill_color=color, back_color=bgcolor)  # "#23dda0"

    fo.checkDataDir(OUTPUTDIR)
    fname = OUTPUTDIR + fname

    # check if the filename is already taken. If so, add counter to the filename.
    fname = save_with_unique_filename(fname)

    if os.path.exists(fname):
        st.error(
            f"Attention: The file, {fname}, already exists! Please change the filename above."
        )
    else:
        img.save(fname)
        st.success(f"Saved file as {fname}")

    return fname


# end of saveFile()


def save_with_unique_filename(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return file_path  # If file doesn't exist, return the original path

    base, ext = os.path.splitext(file_path)  # Separate file name and extension
    counter = 1  # Start counting from 1

    while True:
        # Format the new file name with a number, e.g., file_01.txt
        new_filename = f"{base}_{counter:02d}{ext}"

        if not os.path.exists(new_filename):
            return new_filename  # Return new filename if it doesn't exist
        counter += 1  # Increment counter to try the next number


def app():
    """Streamlit main app function."""
    # App title and description
    st.title("Hey! It's MyQR: An Interactive QR Code Generator!")
    st.write("Generate QR codes with customizable styles!")

    # User input for QR code data
    data = st.text_input(
        "Enter the data for the QR Code:", "https://www.oliverbonhamcarter.com"
    )

    suggestedFileName = "myQRCode.png"

    # # User input for file name
    fname = st.text_input("Enter the filename to save the QRcode", suggestedFileName)

    # Customization options for the QR code
    color = st.color_picker("Select QR Code color", "#23dda0")  # Default color is cyan
    bgcolor = st.color_picker(
        "Select Background color", "#0E228E"
    )  # Default background is navy
    box_size = st.slider(
        "Select Box Size", min_value=1, max_value=20, value=10
    )  # Default box size is 10
    border = st.slider(
        "Select Border Size", min_value=1, max_value=10, value=4
    )  # Default border size is 4

    # Generate the QR code when the button is clicked
    if st.button("Generate QR Code"):
        if data:
            qr_img = generate_qrcode(data, color, bgcolor, box_size, border, fname)
        else:
            st.warning("Please enter some data to generate the QR code!")


# end of app()

if __name__ == "__main__":
    app()
