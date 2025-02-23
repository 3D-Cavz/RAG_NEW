import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/search/"  # Change this if running on a different server

st.title("RAG + YouTube Search System")

query = st.text_input("Enter your search query:")

if st.button("Search"):
    if query:
        with st.spinner("Searching..."):
            response = requests.get(API_URL, params={"query": query})
            if response.status_code == 200:
                data = response.json()
                
                st.subheader("RAG System Results")
                rag_results = data.get("rag_results", [])
                if isinstance(rag_results, list) and rag_results:
                    for i, result in enumerate(rag_results):
                        if isinstance(result, dict):
                            score = result.get("score", "N/A")
                            content = result.get("content", "No content available.")
                            source = result.get("metadata", {}).get("source", "Unknown source")
                            page = result.get("metadata", {}).get("page_label", "Unknown page")
                            st.write(f"**Result {i+1}:**")
                            st.write(f"**Score:** {score}")
                            st.write(f"**Content:** {content}")
                            st.write(f"**Source:** {source} (Page {page})")
                            st.write("---")
                        else:
                            st.write(f"{i+1}. {result}")
                else:
                    st.write("No relevant results found.")
                
                st.subheader("YouTube Search Results")
                youtube_results = data.get("youtube_results", {})
                
                if isinstance(youtube_results, dict):  # Single result case
                    if "error" in youtube_results:
                        st.error(youtube_results["error"])
                    else:
                        st.write(f"1. [{youtube_results['title']}]({youtube_results['url']})")
                elif isinstance(youtube_results, list):  # Multiple results
                    for i, video in enumerate(youtube_results):
                        st.write(f"{i+1}. [{video['title']}]({video['url']})")
            else:
                st.error("Error fetching results. Please try again.")
    else:
        st.warning("Please enter a query before searching.")
