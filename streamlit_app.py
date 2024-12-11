import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit App
st.title("QR Code Generator")

st.write("Enter a URL below to generate a QR code:")

# Input for URL
url = st.text_input("URL", "https://")

if st.button("Generate QR Code"):
    if url and url.startswith("http"):
        # Generate QR code
        qr_code_image = generate_qr_code(url)
        
        # Display QR code
        st.image(qr_code_image, caption="Generated QR Code", use_column_width=True)
        
        # Provide download link
        buf = BytesIO()
        qr_code_image.save(buf, format="PNG")
        byte_data = buf.getvalue()
        st.download_button(
            label="Download QR Code",
            data=byte_data,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Please enter a valid URL starting with http or https.")
