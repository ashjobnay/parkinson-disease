import streamlit as st
print("hello world")
st. title("parkinson disease")


uploaded_files = st.file_uploader("Choose a jpg file", type='jpg')
# for uploaded_file in uploaded_files:
#     st.write("filename:", uploaded_file.name)
if uploaded_files is not None:
    st.image(uploaded_files, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')