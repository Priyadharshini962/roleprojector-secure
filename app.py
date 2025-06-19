import streamlit as st
import cohere
import os

# Initialize Cohere client using the environment variable
co = cohere.Client(os.environ["COHERE_API_KEY"])

# Streamlit app title
st.title("RoleProjector: Generate Project Ideas from Job Descriptions")

# Text input
job_description = st.text_area("Paste a Job Description:", height=250)

# Submit button
if st.button("Generate Project Ideas"):
    if job_description.strip() == "":
        st.warning("Please enter a job description.")
    else:
        try:
            response = co.generate(
                model='command',  # ✅ Correct model for generate API
                prompt=f"Based on the following job description, suggest 3 simple project ideas:\n\n{job_description}\n\nProject Ideas:",
                max_tokens=150,
                temperature=0.7
            )

            # Display result
            st.subheader("Project Ideas")
            st.write(response.generations[0].text.strip())

        except Exception as e:
            st.error(f"Something went wrong: {e}")
