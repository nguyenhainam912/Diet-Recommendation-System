import streamlit as st
from st_pages import Page, show_pages, add_page_title

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

show_pages(
    [
        Page("hello.py", "Home", "🏠"),
        Page("app.py", "Custom Food Recommendation", "🔍"),
    ]
)

st.write("# Welcome to Diet Recommendation System! 👋")

reverse_text_html = f"""
<div >
    <div style="text-align: right;">
        <span>Nhóm 8 Hệ Trợ Giúp Quyết Định</span>
        <br>
        <span>Lớp 21CN5</span>
    </div>
  <ul style="text-align: left;">
    Thành Viên
    <li>Bùi Đào Đại Nghĩa</li>
    <li>Phạm Thế Tài</li>
    <li>Nguyễn Văn Trung</li>
    <li>Trần Anh Phương</li>
    <li>Nguyễn Hải Nam</li>
  </ul>
</div>
"""

st.markdown(reverse_text_html, unsafe_allow_html=True)
