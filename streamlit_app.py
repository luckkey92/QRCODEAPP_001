mport streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(text, fill_color="black", back_color="white"):
qr = qrcode.QRCode(
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=4,
)
qr.add_data(text)
qr.make(fit=True)
qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
return qr_image
def main():
st.title("QR 코드 생성기")
# 사용자 입력
text_input = st.text_input("QR 코드로 변환할 텍스트를 입력하세요:", "<https://www.example.com>")

# 색상 선택
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("QR 코드 색상", "#000000")
with col2:
    back_color = st.color_picker("배경 색상", "#FFFFFF")

if st.button("QR 코드 생성"):
    if text_input:
        # QR 코드 생성
        qr_image = generate_qr_code(text_input, fill_color, back_color)

        # 이미지를 바이트로 변환
        img_byte_arr = io.BytesIO()
        qr_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # QR 코드 표시
        st.image(img_byte_arr, caption="생성된 QR 코드")

        # 다운로드 버튼
        st.download_button(
            label="QR 코드 다운로드",
            data=img_byte_arr,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("텍스트를 입력해주세요.")
        if **name** == "**main**":
main()
