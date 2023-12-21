import streamlit as st
from openai import OpenAI

client = OpenAI(api_key='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')


def cover_letter_generator(job_description, user_background):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a professional cover letter for a job application based on the following job description and applicant's background:\n\nJob Description:\n{job_description}\n\nApplicant's Background:\n{user_background}"},
        ],
        temperature = 0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

def main():
    st.title("AI-Powered Cover Letter Builder")

    with st.form("cover_letter_form"):
        job_description = st.text_area("Job Description", height=150)
        user_background = st.text_area("Your Background", height=150)
        submit_button = st.form_submit_button("Generate Cover Letter")

    if submit_button and job_description and user_background:
        cover_letter = cover_letter_generator(job_description, user_background)
        st.subheader("Generated Cover Letter:")
        st.write(cover_letter)

if __name__ == "__main__":
    main()