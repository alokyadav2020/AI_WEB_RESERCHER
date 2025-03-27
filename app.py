import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

# Streamlit app title
st.title("AI Web Researcher")

# Input fields for user prompt and source URL
prompt = """ **Business Description:** Detailed overview of the company's history, mission, and vision.( 2-3 lines) 
             **Organizational Structure:** Visual representation of the company's hierarchy.( 2-3 lines)  
             **Product/Service Offerings:** Comprehensive list and description of products or services.( 2-3 lines)

"""
source_url = st.text_input("Enter the source URL:")

# Input field for OpenAI API key
api_key = st.text_input("Enter your OpenAI API key:", type="password")

# Configuration for the scraping pipeline
graph_config = {
    "llm": {
        "api_key": api_key,
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

# Button to start the scraping process
if st.button("Scrape"):
    if source_url and api_key:
        # Create the SmartScraperGraph instance
        smart_scraper_graph = SmartScraperGraph(
            prompt=prompt,
            source=source_url,
            config=graph_config
        )

        # Run the pipeline
        result = smart_scraper_graph.run()

        # Display the result
        st.write(result)
    else:
        st.error("Please provide all the required inputs.")

# Instructions for the user
st.markdown("""
### Instructions

1. Enter the source URL from which you want to extract the information.
2. Enter your OpenAI API key.
3. Click on the "Scrape" button to start the scraping process.
""")