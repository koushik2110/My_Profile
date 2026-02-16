import streamlit as st

st.set_page_config(page_title="Koushik M S | GenAI Backend Developer", layout="wide")

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Spectral:wght@600;700&display=swap');

:root {
  --bg: #f8f1e9;
  --bg-2: #f2e7dc;
  --ink: #1f1a17;
  --muted: #5f5a55;
  --accent: #b24d2d;
  --accent-2: #f2b48b;
  --card: #fffdf8;
  --card-strong: #ffffff;
  --border: #eadfce;
  --shadow: rgba(178, 77, 45, 0.14);
}

html, body, [class*="css"]  {
  font-family: 'Space Grotesk', sans-serif;
  color: var(--ink);
}

.stApp {
  background: linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
}

section[data-testid="stSidebar"] {
  background: var(--card);
  border-right: 1px solid var(--border);
}

section[data-testid="stSidebar"] * {
  color: var(--ink);
}

section[data-testid="stSidebar"] [role="switch"] {
  background-color: #bfbfbf !important;
  border: 1px solid #a6a6a6 !important;
}

section[data-testid="stSidebar"] [role="switch"]:hover {
  background-color: #9a9a9a !important;
  border-color: #7f7f7f !important;
}

section[data-testid="stSidebar"] [role="switch"][aria-checked="true"] {
  background-color: #b3b3b3 !important;
  border-color: #9c9c9c !important;
}

section[data-testid="stSidebar"] [role="switch"] > div {
  background-color: #ffffff !important;
  box-shadow: 0 0 0 1px #c9c9c9;
}

.section {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 24px 26px;
  box-shadow: 0 16px 40px var(--shadow);
  margin-bottom: 20px;
}

.section-center {
  text-align: center;
}

.hero-title {
  font-family: 'Spectral', serif;
  font-size: 52px;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 1.05;
}

.hero-role {
  font-size: 18px;
  color: var(--accent);
  font-weight: 600;
  margin-top: 6px;
}

.hero-summary {
  color: var(--muted);
  font-size: 16px;
  margin-top: 14px;
  max-width: 680px;
}

.section-title {
  font-family: 'Spectral', serif;
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--ink);
}

.muted {
  color: var(--muted);
}

body, .stApp, .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span,
.stMarkdown div, .stText, .stCaption, .stSubheader, .stHeader, .stTitle,
h1, h2, h3, h4, h5, h6, p, li {
  color: var(--ink);
}

.card-title {
  font-weight: 600;
  margin-bottom: 6px;
}

.contact-grid {
  display: grid;
  grid-template-columns: max-content 1fr;
  column-gap: 16px;
  row-gap: 10px;
  align-items: center;
  font-size: 14px;
}

.contact-label {
  color: var(--muted);
  white-space: nowrap;
}

.contact-value {
  color: var(--ink);
  word-break: break-word;
}

.contact-value a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

@media (max-width: 640px) {
  .contact-grid {
    grid-template-columns: 1fr;
    row-gap: 6px;
  }
  .contact-label {
    font-weight: 600;
  }
}

.link a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

.chip {
  border: 1px solid #ead3c4;
  background: #fff4ec;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
}

.role {
  font-weight: 600;
  font-size: 16px;
}

.meta {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 10px;
}

ul {
  padding-left: 18px;
  margin: 8px 0 0 0;
}

li {
  margin: 6px 0;
}

.metric-card {
  background: var(--card-strong);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 14px 16px;
  box-shadow: 0 12px 28px rgba(15, 76, 92, 0.08);
  text-align: center;
}

.metric-value {
  font-size: 22px;
  font-weight: 700;
  color: var(--accent);
}

.metric-label {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
}

.metric-row-spacer {
  height: 16px;
}

.project-title {
  font-weight: 700;
  font-size: 16px;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
}

@media (max-width: 900px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
}

.divider {
  height: 1px;
  background: var(--border);
  margin: 14px 0;
}

</style>
""",
    unsafe_allow_html=True,
)

st.sidebar.header("Theme")
dark_mode = st.sidebar.toggle(
    "Dark mode",
    value=False,
    help="Switch to a low-glare dark theme.",
)

if dark_mode:
    st.markdown(
        """
<style>
:root {
  --bg: #0f1113;
  --bg-2: #13171b;
  --ink: #f4f1ec;
  --muted: #c7bdb3;
  --accent: #f0a57b;
  --accent-2: #b24d2d;
  --card: #161a1f;
  --card-strong: #222a33;
  --border: #2a2f36;
  --shadow: rgba(0, 0, 0, 0.45);
}
body, .stApp, .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span,
.stMarkdown div, .stText, .stCaption, .stSubheader, .stHeader, .stTitle,
h1, h2, h3, h4, h5, h6, p, li {
  color: var(--ink);
}
.muted {
  color: var(--muted);
}
.chip {
  border: 1px solid #3a2f28;
  background: #1f1a17;
}
.metric-card {
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
  border: 1px solid #3a2f28;
}
.metric-value {
  color: #ffd3b5;
}
.metric-label {
  color: #e3d5c8;
}
.section {
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
}
.link a {
  color: var(--accent);
}
</style>
""",
        unsafe_allow_html=True,
    )


def bullet_list(items: list[str]) -> str:
    return "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"


def chips(items: list[str]) -> str:
    return "<div class='chips'>" + "".join([f"<span class='chip'>{item}</span>" for item in items]) + "</div>"


def metric_card(value: str, label: str) -> str:
    return (
        "<div class='metric-card'>"
        f"<div class='metric-value'>{value}</div>"
        f"<div class='metric-label'>{label}</div>"
        "</div>"
    )


summary = (
    "GenAI Backend Developer focused on designing and building intelligent backend systems that "
    "leverage LLMs, vector search, and RAG architectures to solve complex enterprise problems. "
    "Experienced in integrating GenAI pipelines with cloud platforms, optimizing ingestion and retrieval "
    "workflows, handling large unstructured datasets, and delivering secure, scalable backend services."
)

experience_bullets = [
    "Database Optimization: Migrated from a customer-specific database architecture to a multi-tenant model using 4 common databases. This reduced database costs by over 40%.",
    "Performance Enhancement: Implemented server-side pagination for high-volume APIs, improving response time from 2 seconds to 250ms.",
    "Query Cost Reduction: Optimized database queries by eliminating unnecessary aggregation lookups, reducing Cosmos DB request unit (RU) consumption by 10-20%.",
    "Caching Strategy: Integrated Redis in-memory caching for frequently accessed configuration data, improving performance and reducing load on the database.",
    "API Architecture Improvements: Refactored heavy internal functions into standalone APIs and scheduled them with Azure Logic Apps cron jobs, improving response time and system reliability.",
    "Automation of Customer Onboarding: Designed and developed new APIs and a UI interface to automate customer and user onboarding processes, cutting manual onboarding time by 30-40 minutes per customer.",
    "Client Interaction and Documentation: Regularly collaborated with clients to gather, analyze, and document technical and business requirements, ensuring successful and timely feature delivery.",
]

project_oci_bullets = [
    "Designed and implemented a GenAI-based log analysis system to automatically identify issues and generate remediation recommendations from OCI logs.",
    "Built an end-to-end RAG (Retrieval Augmented Generation) pipeline using LangChain, vector embeddings, and LLMs for intelligent log analysis.",
    "Automated ingestion of the last 7 days of OCI logs, including errors, warnings, audit events, and system failures across multiple services and regions.",
    "Implemented log preprocessing and overlapping chunking to remove noise and improve semantic understanding during similarity search.",
    "Generated high-quality vector embeddings using gpt-text-embedding-3-large and stored them in Milvus for scalable and fast vector search.",
    "Enabled semantic similarity search to retrieve the top relevant log chunks based on user queries or log IDs.",
    "Integrated GPT-5.2 to perform root cause analysis and generate clear, step-by-step remediation recommendations.",
    "Reduced log investigation time and manual debugging effort while improving security by avoiding direct access to OCI services.",
]

project_bpmn_bullets = [
    "Designed and implemented a GenAI-based solution to analyze SAP BPMN process diagrams and automatically generate standardized process documentation, eliminating manual effort and SAP expert dependency.",
    "Built a pipeline to ingest BPMN process diagrams in XML format, leveraging the hierarchical structure of XML for accurate preprocessing and analysis.",
    "Implemented structured XML preprocessing to remove unnecessary tags and irrelevant data, improving input quality for downstream GenAI processing.",
    "Designed and implemented a structured chunking mechanism to handle large BPMN files, preserving semantic relationships between tags (lanes, tasks, events, gateways) while overcoming LLM token limitations.",
    "Optimized LLM usage by analyzing user queries, identifying relevant BPMN sections, and sending only the required XML chunks to the model, reducing cost and improving response accuracy.",
    "Developed a query-based BPMN analysis feature that allows users to ask process-related questions and receive accurate, context-aware insights from BPMN data.",
    "Implemented automated document generation by processing BPMN sections with specialized prompts and generating standardized documentation using the Python docx library.",
    "Evaluated multiple LLMs and finalized Granite-3.1-8B for its strong understanding of structured XML data and support for large context windows (16K-32K tokens).",
    "Reduced manual BPMN analysis effort, improved scalability, and achieved cost savings through GenAI-driven automation.",
]

skills_core = [
    "Python",
    "JavaScript",
    "Java",
    "FastAPI",
    "Node.js",
    "Express.js",
    "Microservices",
    "RESTful API",
]

skills_genai_ml = [
    "AI (GenAI)",
    "Machine Learning",
    "Supervised Learning",
    "Unsupervised Learning",
    "Deep Learning",
    "RAG",
    "LangChain",
    "Prompt Engineering",
    "Fine-Tuning",
    "NLTK",
    "TensorFlow",
    "Keras",
    "Scikit-learn",
]

skills_data = [
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
]

skills_db = [
    "Mongo DB",
    "Milvus",
    "Mongoose",
    "Redis",
    "Kafka",
    "MySQL",
    "Cosmos DB",
]

skills_cloud_devops = [
    "AWS",
    "S3",
    "Azure",
    "App Services",
    "Function App",
    "Key Vaults",
    "Storage Account",
    "AKS",
    "API Management Service",
    "Docker",
    "K8s",
]

skills_tools = [
    "GIT",
    "GitHub",
    "Splunk",
    "Mongo Compass",
    "Postman",
    "MySQL Workbench",
    "Application Insight",
    "VS Code",
    "Eclipse",
    "Redis Insight",
    "NoSQL Booster",
]


col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown(
        f"""
<div class="section">
  <div class="hero-title">Koushik M S</div>
  <div class="hero-role">GenAI Backend Developer</div>
  <div class="hero-summary">{summary}</div>
</div>
""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
<div class="section">
  <div class="section-title">Contact</div>
  <div class="contact-grid">
    <div class="contact-label">Email</div>
    <div class="contact-value">koushikms21102000@gmail.com</div>
    <div class="contact-label">Phone</div>
    <div class="contact-value">+91 9514148569</div>
    <div class="contact-label">Portfolio</div>
    <div class="contact-value"><a href="https://myprofile-mskoushik.streamlit.app/" target="_blank">My_Profile</a></div>
    <div class="contact-label">GitHub</div>
    <div class="contact-value"><a href="https://github.com/koushik2110" target="_blank">My_Codebase</a></div>
    <div class="contact-label">GeeksforGeeks</div>
    <div class="contact-value"><a href="https://www.geeksforgeeks.org/profile/msk07333?tab=activity" target="_blank">My_coding_Profile</a></div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


st.markdown('<div class="section"><div class="section-title">Impact Highlights</div>', unsafe_allow_html=True)
metric_cols = st.columns(4, gap="medium")
metric_values = [
    ("40%+", "DB cost reduction"),
    ("2s to 250ms", "API response time"),
    ("10-20%", "Cosmos DB RU reduction"),
    ("30-40 mins", "Onboarding time saved"),
]
for col, (value, label) in zip(metric_cols, metric_values):
    with col:
        st.markdown(metric_card(value, label), unsafe_allow_html=True)
st.markdown("<div class='metric-row-spacer'></div>", unsafe_allow_html=True)
project_cols = st.columns(4, gap="medium")
project_metrics = [
    ("RAG Pipeline", "OCI log analysis"),
    ("7-Day Ingestion", "OCI logs automated"),
    ("XML Chunking", "SAP BPMN parsing"),
    ("Docx Automation", "BPMN documentation"),
]
for col, (value, label) in zip(project_cols, project_metrics):
    with col:
        st.markdown(metric_card(value, label), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    f"""
<div class="section">
  <div class="section-title">Work Experience</div>
  <div class="role">IBM | GenAI Backend Developer</div>
  <div class="meta">September 2022 - Current</div>
  <div class="muted">
    As a GenAI Backend Developer, I focus on designing and building intelligent backend systems that
    leverage LLMs, vector search, and RAG architectures to solve complex enterprise problems. My work
    involves integrating GenAI pipelines with cloud platforms, optimizing data ingestion and retrieval
    workflows, handling large unstructured datasets, and implementing secure, scalable backend services.
    I collaborate closely with stakeholders to deliver AI-driven solutions that reduce manual effort,
    improve operational efficiency, and enable faster, more accurate decision-making.
  </div>
  {bullet_list(experience_bullets)}
</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    f"""
<div class="section">
  <div class="section-title">Key Projects</div>
  <div class="projects-grid">
    <div>
      <div class="project-title">GenAI-Based OCI Log Analysis and Recommendation System</div>
      {bullet_list(project_oci_bullets)}
    </div>
    <div>
      <div class="project-title">GenAI-Based SAP BPMN Documentation System</div>
      {bullet_list(project_bpmn_bullets)}
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    f"""
<div class="section">
  <div class="section-title">Technical Skills</div>
  <div class="card-title">Programming and Backend</div>
  {chips(skills_core)}
  <div class="divider"></div>
  <div class="card-title">GenAI and Machine Learning</div>
  {chips(skills_genai_ml)}
  <div class="divider"></div>
  <div class="card-title">Data and Analytics</div>
  {chips(skills_data)}
  <div class="divider"></div>
  <div class="card-title">Databases and Messaging</div>
  {chips(skills_db)}
  <div class="divider"></div>
  <div class="card-title">Cloud and DevOps</div>
  {chips(skills_cloud_devops)}
  <div class="divider"></div>
  <div class="card-title">Tools and Platforms</div>
  {chips(skills_tools)}
</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """
<div class="section">
  <div class="section-title">Education</div>
  <div class="role">Anna University - Madras Institute of Technology</div>
  <div class="meta">Chennai, Tamil Nadu, India | June 2018 - June 2022</div>
  <div>Bachelor of Engineering in Electronics and Communication</div>
  <div class="muted">CGPA: 8.03 / 10</div>
</div>
""",
    unsafe_allow_html=True,
)


awards = [
    "Received a $500 USD cash award and eCard as recognition for driving client delight and contributing to IBM's Base Account Growth initiative by leveraging application expertise and client relationships to help expand business.",
    "IBM Generative AI Foundations (Developed an automated multilingual toxic comment detection system using GPT-4o, handling language detection, translation, toxicity analysis, and conditional MongoDB storage, reducing manual moderation by 90%).",
    "Microsoft Certified: Azure AI Fundamentals.",
]

st.markdown(
    f"""
<div class="section">
  <div class="section-title">Awards and Certifications</div>
  {bullet_list(awards)}
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="section muted section-center">
  Professional profile presentation for enterprise-grade AI and backend systems.
</div>
""",
    unsafe_allow_html=True,
)
