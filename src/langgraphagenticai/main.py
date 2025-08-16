import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agentic_app():
    """
    Loads and runs the LangGraph AngeticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM Model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    
    """

    ##Load UI
    UI=LoadStreamlitUI()
    user_input=UI.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Initialize and display chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display existing chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    user_message = st.chat_input("Enter your message:")

    
    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            #Initialize and set up the graph based on use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return

            ##Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Graph set up failed- {e}")
                return
            

        except Exception as e:
            st.error(f"Error: Graph set up failed- {e}")
            return