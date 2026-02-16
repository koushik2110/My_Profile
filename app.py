import streamlit as st

st.set_page_config(page_title="Koushik M S | GenAI Backend Developer", layout="wide")

# HEADER
st.title("Koushik M S")
st.subheader("GenAI Backend Developer")

st.write("""
📧 koushikms21102000@gmail.com  
📱 +91 9514148569  
""")

st.divider()

# ABOUT
st.header("About Me")
st.write("""
GenAI Backend Developer with experience in building intelligent backend systems using
LLMs, vector search, RAG pipelines, and cloud-native architectures.
Focused on scalable APIs, data pipelines, and AI-driven automation.
""")

# SKILLS
st.header("Technical Skills")

skills = [
"Python","JavaScript","Java","FastAPI","Node.js","Express.js",
"Machine Learning","Deep Learning","LangChain","RAG",
"MongoDB","Milvus","Redis","Kafka","MySQL",
"AWS","Azure","Docker","Kubernetes"
]

st.write(", ".join(skills))

# EXPERIENCE
st.header("Work Experience")

st.subheader("IBM — GenAI Backend Developer (Sep 2022 – Present)")

st.markdown("""
- Migrated to multi-tenant DB architecture → **40% cost reduction**
- Improved API response from **2s → 250ms**
- Reduced Cosmos DB RU usage by **10–20%**
- Implemented Redis caching for performance
- Automated customer onboarding saving **30–40 min/customer**
""")

# PROJECTS
st.header("Projects")

st.subheader("OCI Log Analysis & Recommendation System")
st.markdown("""
- Built **RAG pipeline** with LangChain + vector search  
- Generated embeddings & stored in **Milvus**  
- Used LLMs for root-cause analysis & remediation suggestions  
""")

st.subheader("SAP BPMN GenAI Documentation System")
st.markdown("""
- Parsed BPMN XML diagrams
- Built structured chunking for LLM input
- Automated documentation generation using Python
""")

# EDUCATION
st.header("Education")
st.write("""
**Anna University – Madras Institute of Technology**  
B.E Electronics & Communication — CGPA: 8.03
""")

# CERTIFICATIONS
st.header("Certifications & Awards")
st.markdown("""
- IBM Generative AI Foundations  
- Microsoft Azure AI Fundamentals  
- IBM Client Delight Award ($500)
""")

# FOOTER
st.divider()
st.caption("Built with Streamlit")
