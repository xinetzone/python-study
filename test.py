from PIL import Image
from matplotlib import pyplot as plt
import streamlit as st


def read_markdown_file(markdown_file):
    with open(markdown_file, encoding='utf-8') as fp:
        w = fp.read()
    return w

## 方案一
intro_markdown = read_markdown_file("intro.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

## 方案二

def latex_tag(tag):
    out = r"$\bf{tag}$"
    return out.replace('tag', str(tag))

fig, ax = plt.subplots()
img = Image.open('images/test.png')
ax.imshow(img)
ax.axis('off')

ax.set_title(f'image {latex_tag("t")} {latex_tag(134)}', loc='center')
st.pyplot(fig)
