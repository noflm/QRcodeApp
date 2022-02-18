import streamlit as st
import qrcode as qr


st.title('QRコード生成')
url = st.text_input('URLを入力してください')

if st.button('QRコードを生成'):
    if url:
        img = qr.make(url)
        st.image(img.get_image(), width=500)
    else:
        st.write('URLを入力してください')