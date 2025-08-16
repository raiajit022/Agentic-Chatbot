import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message
        
        if usecase == "Basic_Chatbot":
            # Add user message to chat history and display it
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            with st.chat_message("user"):
                st.write(user_message)
            
            # Process and get assistant response
            try:
                for event in graph.stream({'messages': [("user", user_message)]}):
                    for value in event.values():
                        if 'messages' in value:
                            assistant_response = value['messages'].content
                            # Add assistant response to chat history and display it
                            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
                            with st.chat_message("assistant"):
                                st.write(assistant_response)
            except Exception as e:
                st.error(f"Error processing message: {e}")
