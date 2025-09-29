import streamlit as st
# st.pdf("Maheswar_Sahu_Resume_SDSM.pdf",height=600)

# ==== Basic Info ====
st.set_page_config(page_title="Maheswar Sahu — CV", layout="centered")
st.title("Maheswar Sahu")
st.write("Mississauga, ON, Canada  |  📞 1 647 333-8614  |  ✉️ f1mahesh@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/maheswar-sahu)")

with open("Maheswar_Sahu_Resume_SDSM.pdf", "rb") as pdf_file:
    st.download_button(label="Download CV (PDF)", data=pdf_file, file_name="Maheswar_Sahu_Resume_SDSM.pdf", mime="application/pdf")

# ==== Tabs ====
tabs = st.tabs(["Profile", "Skills", "Experience", "Achievements", "Education"])

with tabs[0]:
    st.subheader("Profile")
    st.write("""
    **Senior Data Science Manager** with 14 years of experience delivering data-driven innovation and architecting large-scale enterprise applications. 
    Combines strong analytical skills and practical understanding of data flow to identify business opportunities and drive measurable outcomes.
    - Skilled in SQL, Python, R, Machine Learning, GenAI agent/model design, and data curation.
    - Proven in system design, performance optimization, and advanced debugging.
    - Strong Life Sciences domain knowledge, leveraging ClinicalTrials.gov for analytics.
    """)

with tabs[1]:
    st.subheader("Technical Skills")
    st.write("""
    - **Languages/Libraries:** JAVA/J2EE, JavaScript, Spring, Python, R, SQL, PySpark, Pandas, NumPy  
    - **Databases/Warehouses:** Oracle, MySQL, PostgreSQL, Snowflake, Databricks, Pinecone, Chroma
    - **Tools/Platforms:** Datadog, Streamlit, Liferay, Alfresco, Gen AI
    - **Cloud:** AWS, Azure, GCP
    - **Data Sources:** AACT ClinicalTrials.gov, PubMed
    """)
    st.subheader("Soft Skills")
    st.write("""
    - Problem-Solving, Resourcefulness, Leadership, Ownership, Communication, Teamwork, Strategic & Critical Thinking, Time Management, Data Storytelling
    """)

with tabs[2]:
    st.subheader("Professional Experience")
    st.markdown("#### Cognizant Technology Solutions (Life Sciences & Healthcare)")
    with st.expander("Senior Manager, Data Science (Sep 2025 – Present)"):
        st.write("""
        - Built a data analysis portal for monitoring data flow and predicting trends
        - Applied ML/predictive analytics to optimize workflows/compliance
        - Directed cross-functional teams, translating requirements into data-driven strategies
        """)
    with st.expander("Product Tech Support Manager (Mar 2022 – Aug 2025)"):
        st.write("""
        - Managed support for Shared Investigator Platform (SIP)
        - Conducted data flow analysis, improved incident resolution time and customer satisfaction
        - Embedded analytics into support workflows
        """)
    with st.expander("Senior Associate, Application Dev & Support (Jul 2018 – Feb 2022)"):
        st.write("""
        - Designed/implemented SIP module solutions
        - Led tuning across code & DB layers
        - Supported API development
        """)
    st.markdown("#### Yamaha Motor Solutions India (Telecom)")
    with st.expander("Software Engineer (Dec 2011 – Aug 2014)"):
        st.write("""
        - Offered dev & support leadership
        - Led requirements analysis, solution design, API integrations, and debugging
        """)
    st.markdown("#### Experis IT India (ERP)")
    with st.expander("Software Developer (Mar 2011 – Dec 2011)"):
        st.write("""
        - Developed ERP modules with Struts, JSP, Servlets, Oracle DB
        - End-to-end dev (coding, testing, debugging)
        """)

with tabs[3]:
    st.subheader("Achievements & Impact")
    st.write("""
    - Reduced manual effort by 30% with Python automation
    - Cut ticket volume by 40% with dashboards & workflow fixes
    - Deployed real-time KPI dashboards in Streamlit
    - Enhanced user/product adoption with ML ranking models
    - Created GenAI agent for knowledge base (–10% ticket reduction)
    - Multiple awards: Working as One, Emerging Leader (2018/2019), Specialist, Digital Super Star, Extra Mile
    """)

with tabs[4]:
    st.subheader("Education")
    st.write("""
    **B.Tech, Computer Science Engineering**  
    Orissa Engineering College, India (2006–2010)
    """)
