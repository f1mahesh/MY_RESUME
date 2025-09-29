import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Maheswar Sahu — Senior Data Science Manager",
    layout="wide",
    page_icon=":briefcase:"
)

# --- SIDEBAR ---
with st.sidebar:
    st.image("profile-photo.png", width=130)  # Optional: add your headshot with this filename in the folder
    st.write("## Contact")
    st.write(
        "📍 Mississauga, ON\n"
        "📞 1 647 333-8614\n"
        "✉️ [f1mahesh@gmail.com](mailto:f1mahesh@gmail.com)\n"
        "[LinkedIn Profile](https://www.linkedin.com/in/maheswar-sahu)"
    )
    st.write("## Download")
    with open("Maheswar_Sahu_Resume_SDSM.pdf", "rb") as f:
        st.download_button("Download Full Resume (PDF)", f, file_name="Maheswar_Sahu_Resume_SDSM.pdf")

    st.write("## Quick Navigation")
    st.markdown("""
    - [Profile Summary](#profile-summary)
    - [Skills](#skills)
    - [Professional Experience](#professional-experience)
    - [Achievements](#achievements)
    - [Education](#education)
    - [Awards](#awards)
    """)


# --- HEADER: PROFILE SECTION ---
st.markdown("# Maheswar Sahu")
st.markdown("### Senior Data Science Manager")
st.markdown("---")

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Profile Summary")
    st.write(
        "Senior Data Science Manager with 14 years' experience in delivering data-driven innovation and architecting large-scale enterprise apps. "
        "Strong analytical skills and business acumen, leveraging SQL, Python, R, Machine Learning, GenAI agent/model design, and high-quality data curation. "
        "Domain expertise in Life Sciences, including clinical trials analytics. Proven leader in system design, performance optimization, and debugging."
    )

with col2:
    st.success("Open to opportunities in Data Science leadership, analytics engineering, and innovation roles!")

st.markdown("---")


# --- SKILLS SECTION ---
st.subheader("Skills & Core Competencies")
sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown("**Programming/Libraries**")
    st.write(
        "- JAVA/J2EE\n"
        "- JavaScript\n"
        "- Spring\n"
        "- Python\n"
        "- R\n"
        "- SQL\n"
        "- PySpark\n"
        "- Pandas\n"
        "- NumPy"
    )
with sc2:
    st.markdown("**Databases & Tools**")
    st.write(
        "- Oracle, MySQL, PostgreSQL, Snowflake\n"
        "- Databricks, Pinecone, Chroma\n"
        "- Datadog, Streamlit\n"
        "- Liferay, Alfresco\n"
        "- GenAI"
    )
with sc3:
    st.markdown("**Cloud & Data Sources**")
    st.write(
        "- AWS\n"
        "- Azure\n"
        "- GCP\n"
        "- ClinicalTrials.gov\n"
        "- PubMed"
    )
st.info("Soft skills: Problem-solving • Leadership • Ownership • Communication • Teamwork • Strategic/Critical Thinking • Data Storytelling • Time Management")


st.markdown("---")


# --- EXPERIENCE SECTION ---
st.subheader("Professional Experience")
exp_tabs = st.tabs(["Cognizant", "Yamaha Motor Solutions", "Experis IT India"])

with exp_tabs[0]:
    st.markdown("#### Cognizant Technology Solutions — Life Sciences & Healthcare")
    st.markdown("**Senior Manager, Data Science (Sep 2025 – Present)**")
    st.write(
        "- Built analysis portal for data flow, trend visualization, and outcome prediction\n"
        "- Integrated SIP systems for deeper BI insights\n"
        "- Applied ML/predictive analytics for workflows/decision-making\n"
        "- Led cross-functional teams for enterprise data solutions\n"
        "- Partnered with stakeholders for actionable strategies"
    )
    st.markdown("**Product Tech Support Manager (Mar 2022 – Aug 2025)**")
    st.write(
        "- Managed SIP application and client CTMS integrations\n"
        "- Proactive data flow/incident analysis\n"
        "- Embedded analytics in support workflows\n"
        "- Improved customer satisfaction"
    )
    st.markdown("**Senior Associate, App Dev & Support (Jul 2018 – Feb 2022)**")
    st.write(
        "- Technical solutions for SIP modules\n"
        "- Performance tuning code/DB\n"
        "- API development/integration"
    )
    st.markdown("**Associate Projects (Aug 2014 – Jun 2018)**")
    st.write(
        "- Developed core SIP functionalities\n"
        "- Quality/release compliance\n"
        "- Clinical study workflows"
    )

with exp_tabs[1]:
    st.markdown("#### Yamaha Motor Solutions India — Telecom")
    st.markdown("**Software Engineer (Dec 2011 – Aug 2014)**")
    st.write(
        "- Led technical dev/support for enterprise applications\n"
        "- Collaborated for requirements/solutions\n"
        "- Implemented middleware/API integrations\n"
        "- Debugging and incident reduction"
    )

with exp_tabs[2]:
    st.markdown("#### Experis IT India — ERP")
    st.markdown("**Software Developer (Mar 2011 – Dec 2011)**")
    st.write(
        "- Developed ERP modules (Java/JSP/Servlets/Struts)\n"
        "- Designed Oracle RDBMS layers\n"
        "- End-to-end software dev/test/debug"
    )


# --- ACHIEVEMENTS SECTION ---
st.markdown("---")
st.subheader("Impact & Achievements")
ach_col1, ach_col2 = st.columns(2)
with ach_col1:
    st.write(
        "- Automated Python workflows (–30% manual effort)\n"
        "- Interactive KPI dashboards with Streamlit\n"
        "- User/site ranking models for improved product adoption\n"
        "- Real-time incident dashboards"
    )
with ach_col2:
    st.write(
        "- GenAI agent for knowledge base (–10% ticket volume)\n"
        "- Data integrity dashboards (–40% support tickets)\n"
        "- Alfresco cost savings via architecture analysis\n"
        "- Innovative revenue-preserving workarounds"
    )
st.markdown("---")


# --- EDUCATION ---
st.subheader("Education")
st.write(
    "**B.Tech, Computer Science Engineering**\n"
    "Orissa Engineering College, India (2006–2010)"
)


# --- AWARDS SECTION ---
st.markdown("---")
st.subheader("Awards & Recognition")
st.write(
    "- **Working as One** (Cognizant TriZetto Life Sciences, Q2 2025) — Executive analytics dashboard for SIP\n"
    "- **Emerging Leader Award** (Cognizant Life Sciences, Q4 2018 & Q4 2019) — Leadership & client impact\n"
    "- **Specialist Award** (Cognizant Life Sciences, Q1 2018) — Training Module integration\n"
    "- **Digital Super Star Award** (Q3 2015) — Solution delivery & innovation\n"
    "- **Extra Mile Award** (Q1 2016) — Outstanding dedication"
)


# --- FOOTER ---
st.markdown("---")
st.markdown("© 2025 Maheswar Sahu | Designed with Streamlit")

