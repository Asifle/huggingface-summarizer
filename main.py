import streamlit as st
from scrape import scrape_blog
from nlp import summarize_text

# Streamlit App Configuration
st.set_page_config(page_title="Blog Summarizer", layout="centered")

st.title("Blog Summarizer")
st.write("Enter a blog URL, and this app will summarize its content for you!")

# Input field for the blog URL
blog_url = st.text_input("Enter Blog URL:", placeholder="https://example.com/blog")

# Button to trigger summarization
if st.button("Summarize"):
    if blog_url:
        with st.spinner("Fetching blog content..."):
            blog_content, scrape_error = scrape_blog(blog_url)

        if scrape_error:
            st.error(scrape_error)
        else:
            st.success("Blog content fetched successfully!")
            st.write("**Original Blog Content:**")
            st.text_area("Content", blog_content, height=200, disabled=True)

            with st.spinner("Summarizing content..."):
                summary, summary_error = summarize_text(blog_content)

            if summary_error:
                st.error(summary_error)
            else:
                st.success("Summarization complete!")
                st.write("**Summarized Content:**")
                st.text_area("Summary", summary, height=150, disabled=True)

                # Download Option
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="blog_summary.txt",
                    mime="text/plain",
                )
    else:
        st.warning("Please enter a valid blog URL.")
