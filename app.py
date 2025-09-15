import streamlit as st
import pdfplumber
from docx import Document
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
import io
st.title("Visualisation of word cloud and sentiment analysis")
file = st.file_uploader("Upload your file",type = ["docx","pdf"])
if file is not None:
    file_name = file.name
    iobytes = file.read()
    if file_name.lower().endswith(".pdf"):
        doc = pdfplumber.open(io.BytesIO(iobytes))
        pages=[]
        for page in doc.pages:
            pages.append(page.extract_text())
            text =  ' '.join(pages)
    elif file_name.lower().endswith(".docx"):
        doc = Document(io.BytesIO(iobytes))
        paras=[]
        for para in doc.paragraphs:
            paras.append(para.text)
            text =  ' '.join(paras)
    if not text.strip():
        st.error("Text not founded")
    else:
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("WORD CLOUD")
            image = WordCloud(width=800, height=800, background_color="white").generate(text)
            plt.imshow(image)
            plt.axis("off")
            st.pyplot(plt, use_container_width=True)
        with col2:
            st.subheader("SENTIMENT ANALYSIS")
            lines = text.split("\n")
            sentiment = [TextBlob(line).sentiment.polarity for line in lines if line.strip() != '']
            pos = neut = neg = 0
            for score in sentiment:
                if score > 0.1:
                    pos += 1
                elif score < -0.1:
                    neg += 1
                else:
                    neut += 1

            plt.clf()  # clear previous plot
            plt.pie([pos, neut, neg], labels=["Positive", "Neutral", "Negative"], autopct='%1.1f%%', colors=["green", "gold", "red"])
            st.pyplot(plt, use_container_width=True)
            

