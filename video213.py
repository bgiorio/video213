import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.header("The Best Company")

st.write("""
    Experienced Instructional Designer with over 25 years of expertise in developing engaging, web-based training courses for Ford, GM, Chrysler and the Military. Skilled in collaborating with SMEs to design and develop impactful training solutions using Storyline 360, Rise, Captivate, and Animate CC. Proven track record of improving learner engagement and retention through innovative course development and design.
    """)

st.subheader("Our Team")

# creates space inbetween the columns
col1, col2, col3 = st.columns(3)

# Use the correct separator
df = pd.read_csv("C:/Brad/Python/Video213Project/data.csv", sep=",")

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Optional: Show column names for debugging
# st.write("Columns found:", df.columns.tolist())

with col1:
    for index, row in df[:4].iterrows():  # rows 0 to 3
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():  # rows 4 to 7
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():  # rows 8 and beyond
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

#

