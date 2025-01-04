import streamlit as st
from scrape import scrape_blog
from nlp import summarize_text

# Streamlit App Configuration
st.set_page_config(page_title="📰 AI Blog Summarizer", layout="wide")

# Header Section
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.5em;
        color: #4CAF50;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2em;
        color: #6c757d;
    }
    </style>
    <h1 class="main-title">📰 Blog Summarizer</h1>
    <p class="sub-title">Enter a blog URL, and this app will summarize its content for you!</p>
    """,
    unsafe_allow_html=True,
)

# Input Section
st.write("---")
st.header("Enter Blog URL")
blog_url = st.text_input(
    "Provide the URL of the blog you want to summarize:",
    placeholder="https://example.com/blog",
)

# Summarize Button
if st.button("🔍 Summarize Blog"):
    if blog_url:
        # Scraping the Blog
        with st.spinner("🚀 Fetching blog content..."):
            blog_content, scrape_error = scrape_blog(blog_url)

        if scrape_error:
            st.error(f"❌ {scrape_error}")
        elif not blog_content or len(blog_content.strip()) < 100:
            st.warning("⚠️ Blog content is too short or could not be retrieved.")
        else:
            st.success("✅ Blog content fetched successfully!")
            st.write("### Original Blog Content")
            st.text_area("Full Blog Content", blog_content, height=250, disabled=True)

            # Summarizing the Blog
            with st.spinner("✨ Summarizing content..."):
                summary, summary_error = summarize_text(blog_content)

            if summary_error:
                st.error(f"❌ {summary_error}")
            else:
                st.success("✅ Summarization complete!")
                st.write("### Summarized Content")
                st.text_area("Summary", summary, height=200, disabled=True)

                # Download Option
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="blog_summary.txt",
                    mime="text/plain",
                )
    else:
        st.warning("⚠️ Please enter a valid blog URL.")

# Footer
st.write("---")
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #6c757d;
    }
    </style>
    <p class="footer">Made using Streamlit</p>
    """,
    unsafe_allow_html=True,
)
