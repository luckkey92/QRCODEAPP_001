
import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qrcode(data):
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit App Title
st.title("QR Code Generator")

# Input Section
st.header("Enter the text or URL to generate a QR Code")
input_text = st.text_input("Text or URL", placeholder="Type your text or URL here...")

# Generate Button
if st.button("Generate QR Code"):
    if input_text:
        qr_image = generate_qrcode(input_text)
        
        # Save QR Code to a BytesIO object
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Display QR Code
        st.image(qr_image, caption="Your QR Code", use_column_width=True)

        # Add a download button
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some text or a URL before generating the QR Code.")

# Footer
st.markdown("Made with ❤️ using Streamlit")
