import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.markdown(f"<h1 style='text-align: center;'>🤖 {self.config.get_page_title()}</h1>", unsafe_allow_html=True)


        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API Key to proceed. Don't have? refer : https://console.groq.com/keys ")

            ##Usecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases", usecase_options)
            
            # Add clear chat button
            if st.button("🗑️ Clear Chat History"):
                if "chat_history" in st.session_state:
                    st.session_state.chat_history = []
                st.rerun()

        return self.user_controls



