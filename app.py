import streamlit as st
import cohere
import os

# Use environment variable for secure API key access
co = cohere.Client(os.environ["COHERE_API_KEY"])

st.set_page_config(page_title="RoleProjector", page_icon="🧠")

st.title("🤖 RoleProjector")
st.markdown("Turn job descriptions into custom project ideas for your portfolio.")

job_desc = st.text_area("🔍 Paste a job description below:")

if st.button("🚀 Generate Project Idea"):
    if not job_desc.strip():
        st.warning("Please paste a job description first.")
    else:
        with st.spinner("Thinking... generating ideas..."):
            prompt = f"""
You are an AI that helps job seekers create custom portfolio projects based on job descriptions.

Here is the job description:
{job_desc}

Suggest 1–2 project ideas that:
- Match the required skills
- Can be built in 2–3 weeks
- Are tailored to data-related roles like data analyst, data scientist, data engineer, or business analyst
Include: project title, tools used, and what each project demonstrates.
"""
            try:
                response = co.generate(
                    model='command-r',
                    prompt=prompt,
                    max_tokens=300,
                    temperature=0.8
                )
                result = response.generations[0].text.strip()
                st.success("Here's your custom project idea:")
                st.markdown(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")