from pathlib import Path
import streamlit as st
from PIL import Image

# File paths
css_file = "styles/main.css"
profile_pic = "assets/profile.png"


# Personal details
PAGE_TITLE = "Dipam Soni | Digital Resume"
PAGE_ICON = ":wave:"
NAME = "Dipam Soni"

NAME_ROLE = """
<style>
.large-title {
    font-size: 36px; /* Adjust the size as needed */
    font-weight: bold;
}
.small-bold-text {
    font-size: 18px; /* Adjust the size as needed */
    font-weight: bold;
}
</style>
<div>
    <span class="large-title">Dipam Soni</span><br>
    <span class="small-bold-text">(Data Scientist / Analyst)</span>
</div>
"""

justify_style = """
<style>
.justified-text {
    text-align: justify;
}
</style>
"""

DESCRIPTION = f"""
{justify_style}
<div class="justified-text">
    Data scientist with over 2+ years of practical experience using Python for data science/analysis projects. 
Expertise in advanced machine learning and deep learning, including fine-tuning LLMs for diverse applications.
</div>
"""

QUALIFICATIONS = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>✔️ 2+ Years of experience extracting actionable insights from data</li>
        <li>✔️ Skilled in data visualization with Power BI, Tableau, and Python EDA libraries, effectively presenting insights to various stakeholders.</li>
        <li>✔️ Good understanding of Machine Learning, Deep Learning and their respective applications</li>
        <li>✔️ Experienced in building and maintaining data pipelines and workflows for automating data collection, processing, and analysis, supporting efficient data-driven decisions.</li>
        <li>✔️ Proficient in designing and managing APIs with FastAPI and creating Streamlit dashboards to enhance project workflows.</li>
        <li>✔️ Proven track record of translating business needs into actionable data solutions, optimizing processes, and improving organizational performance.</li>
        <li>✔️ Always ready to learn new concepts and challenges for improving self-knowledge.</li>
    </ul>
</div>
"""

SKILLS = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>👩‍💻 Programming: Python (Scikit-learn, transformers, tensorflow, pytorch, Pandas, many more), SQL, R</li>
        <li>📊 Data Visualization: PowerBi, MS Excel, Plotly</li>
        <li>📚 Machine Learning with Python: Regression, Classification, Clustering</li>
        <li>♾ Deep Learning with Python: CNN, RNN, GAN, RAG, LSTM, Autoencoders</li>  
        <li>🗄️ Data Warehousing: MongoDB, MySQL, PostgreSQL, ORACLE, Microsoft SQL server</li>
        <li>🔍 API: Flask, FastAPI, Streamlit</li>
    </ul>
</div>
"""

EXP1 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Utilized FastAPI across all specified projects and managed different types of API response handling with 
databases.</li>
        <li>► Designed Streamlit dashboards for multiple projects, incorporating data visualization through 
Plotly (Python), as well as PowerBI and Tableau dashboards.</li>
    </ul>
</div>
"""

EXP2 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Created and maintained data pipelines and workflows to automate data collection, processing, and analysis, 
reducing manual effort.</li>
        <li>► Various ML and DL models for all types of industries and domain data.</li>
        <li>► More models at same time to perform, <b>No code machine learning and deep learning tool</b>.</li>
    </ul>
</div>
"""

EXP3 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Developed capabilities such as rewording existing content to avoid plagiarism, generating new content based 
on specific keywords, and creating and posting articles tailored to different audiences on social media and 
other platforms.</li>
        <li>► Created a model to provide specific answers from submitted content, PDFs, or text excerpts.</li>
        <li>► Implemented live screenshot capturing of targeted websites at user request, with the ability to extract text 
and produce guided or tutorial videos complete with audio.</li>
        <li>► Additionally, created a meeting bot that captures all participants' audio during meetings, creating minutes and automatically generating associated documents.</li>
    </ul>
</div>
"""

EXP4 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Business team facing issues in on time raw delivery. Developing a Time Delivery Prediction system to 
enhance logistics efficiency.</li>
        <li>► Utilizing machine learning algorithms to analyze historical data and factors affecting delivery times, the project aims to provide accurate predictions for timely and reliable shipments.</li>
        <li>► As result increased result to 85% accuracy to 92% to 93% accuracy.</li>
    </ul>
</div>
"""

EXP5 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Natural language processing (NLP) technique used to determine sentiment of employees, customers and vendors feedbacks (like NPS survey, internal & external survey). using vader sentiment analysis python library.</li>
        <li>► Prepared PowerBI dashboard for presenting the result of sentiment analysis.</li>
    </ul>
</div>
"""

EXP6 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► The goal with a project of this scope is to make better data-driven decisions in channel optimization and inventory planning(Capacity of the supplier).</li>
        <li>► Product price & quality comparison with competitors from different suppliers.</li>
        <li>► Sales forecasting for the future trends and B2B supplier demand.</li>
    </ul>
</div>
"""

EXP7 = f"""
{justify_style}
<div class="justified-text">
    <ul>
        <li>► Supplier Reliability, Responsiveness, Agility, External risk (Macro Features), Feature score analysis. Future forecast, analysis and dashboard with Python presented in PowerBI.</li>
        <li>► Supplier capacity and delivery time prediction with classical ML models.</li>
    </ul>
</div>
"""

EMAIL = "sonidipam007@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/dipam-soni-276aa8207/",
    "GitHub": "https://github.com/dipamsoni"
}

CERTIFICATES = {
    "🏆 Accenture Data analytics & visualization": "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Accenture%20North%20America/hzmoNKtzvAzXsEqx8_Accenture%20North%20America_9ZL3JtoANTzpifjpE_1661767436652_completion_certificate.pdf",
    "🏆 Process Data from Dirty to Clean": "https://www.coursera.org/account/accomplishments/certificate/FLHM87KXDXSB",
    "🏆 Learn Python for Data Science & Machine Learning from A-Z": "https://www.udemy.com/certificate/UC-5d603f74-2aa2-46bb-80bc-17d082787945/",
    "🏆 Master Python With NumPy For Data Science & Machine Learning": "https://www.udemy.com/certificate/UC-17208615-e20b-48de-9438-6d26fab4ea68/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # Rotate the image if necessary (e.g., 90 degrees counterclockwise)
    profile_pic = profile_pic.rotate(270, expand=True)
    st.image(profile_pic, width=220)

with col2:
    st.markdown(NAME_ROLE, unsafe_allow_html=True)
    st.write(" ")
    st.markdown(DESCRIPTION, unsafe_allow_html=True)
    st.write(" ")
    st.write("📫", EMAIL)

# SOCIAL LINKS
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# QUALIFICATIONS
st.write('\n')
st.subheader("QUALIFICATIONS")
st.markdown(QUALIFICATIONS, unsafe_allow_html=True)

# SKILLS
st.write('\n')
st.subheader("SKILLS")
st.markdown(SKILLS, unsafe_allow_html=True)

# PROFESSIONAL EXPERIENCE
st.write('\n')
st.subheader("PROFESSIONAL EXPERIENCE")
st.write("---")

st.write("🚧", "**Jr. Data Scientist | Shivohm Softech PVT. LTD.**")
exp1_cols = st.columns(2)
exp1_cols[0].write("**1. Dashboard, ETL process, APIs**")
exp1_cols[1].write("(05/2022 - Present)")
st.markdown(EXP1, unsafe_allow_html=True)

exp2_cols = st.columns(2)
exp2_cols[0].write("**2. AutoML**")
exp2_cols[1].write("(12/2022 - Present)")
st.markdown(EXP2, unsafe_allow_html=True)

exp3_cols = st.columns(2)
exp3_cols[0].write("**3. Artificial Intelligence for Life**")
exp3_cols[1].write("(01/2023 - Present)")
st.markdown(EXP3, unsafe_allow_html=True)

exp4_cols = st.columns(2)
exp4_cols[0].write("**4. On Time Delivery Prediction**")
exp4_cols[1].write("(09/2022 - 04/2023)")
st.markdown(EXP4, unsafe_allow_html=True)

exp5_cols = st.columns(2)
exp5_cols[0].write("**5. NLP tool**")
exp5_cols[1].write("(05/2022 - 12/2023)")
st.markdown(EXP5, unsafe_allow_html=True)

exp6_cols = st.columns(2)
exp6_cols[0].write("**6. Sales & Demand forecasting**")
exp6_cols[1].write("(05/2022 - 05/2023)")
st.markdown(EXP6, unsafe_allow_html=True)

exp7_cols = st.columns(2)
exp7_cols[0].write("**7. Supplier performance matrix analysis**")
exp7_cols[1].write("(05/2022 - 05/2023)")
st.markdown(EXP7, unsafe_allow_html=True)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("CERTIFICATES")
st.write("---")
for project, link in CERTIFICATES.items():
    st.write(f"[{project}]({link})")
