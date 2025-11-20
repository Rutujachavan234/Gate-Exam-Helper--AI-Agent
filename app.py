import streamlit as st
from crew_runner import run_crew
from pdf_generator import generate_pdf
import os

st.set_page_config(page_title="GATE Helper AI", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
<style>
.block {
    background-color: #1E1E1E;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 8px #444;
    color: #E8E8E8;
}
.title {
    font-size: 22px;
    font-weight: 600;
    color: #5FA1FF;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 GATE Exam Helper — AI-Agent")

# Sidebar
branch = st.sidebar.selectbox("Select Branch", 
                              ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil"])

topic = st.text_input("Enter Topic Name", placeholder="Example: Deadlock, OSI Model, Trees...")

# Generate Notes
if st.button("Generate Study Material"):
    if topic.strip() == "":
        st.warning("⚠ Please enter a topic.")
    else:
        with st.spinner("Generating best GATE notes…"):
            output = run_crew(branch, topic)

        st.session_state["full_output"] = output
        sections = output.split("###")

        for part in sections:
            if part.strip() == "":
                continue

            header = part.split("\n")[0].strip()
            content = "\n".join(part.split("\n")[1:]).strip()

            st.markdown(f"<div class='block'><div class='title'>📘 {header}</div>{content}</div>", unsafe_allow_html=True)

        # PDF Download
        pdf_path = generate_pdf(output, "gate_notes.pdf")
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download PDF", f, file_name="GATE_Notes.pdf")

# Chatbot
st.write("---")
st.subheader("💬 Ask Follow-up Questions")

if "chat" not in st.session_state:
    st.session_state["chat"] = []

user_msg = st.text_input("Ask your doubt:")

if st.button("Ask AI"):
    if user_msg.strip():
        reply = run_crew(branch, user_msg)
        st.session_state["chat"].append(("You", user_msg))
        st.session_state["chat"].append(("AI", reply))

for sender, msg in st.session_state["chat"]:
    st.markdown(f"**{sender}:** {msg}")
