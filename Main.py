import streamlit as st
import google.generativeai as genai

def main():
    st.set_page_config(layout="wide")

    # Add background image with CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://i.imgur.com/hhctB94.jpeg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Hamzafy")
    st.markdown('---')
    col1, col2 = st.columns(2)
    with col1:
        st.image('hamzafy.jpg', width=400)
    with col2:
        st.title("🤖Ask Hamza!")
        st.header('🚀Hamzafied AI!')
        st.markdown('---')

    # Load API key securely from secrets.toml
    api_key = st.secrets["gemini_api_key"]

    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')


    system_instruction = ('''
    Your name is Hamza.
    You are a highly intelligent and versatile AI chatbot 
    capable of answering questions from all fields of knowledge, 
    including but not limited to science, technology, history, art, 
    entertainment, and more. You provide accurate, helpful, 
    and respectful responses to all user queries, regardless of the topic. 
    Your responses should be clear, concise, and informative. 
    If you don’t know the answer to a question, politely 
    inform the user and offer to help with something else.
    Respond respectfully if any user prompt is using abusive language
    ''')

    # Function to display roles correctly
    def translate_role(role):
        return "assistant" if role == "model" else role

    # Start session and inject system instruction
    if "chat_session" not in st.session_state:
        chat = model.start_chat(history=[])
        # Send system instruction as hidden first message
        _ = chat.send_message(system_instruction)
        st.session_state.chat_session = chat

    # Show conversation history
    for message in st.session_state.chat_session.history[1:]:
        with st.chat_message(translate_role(message.role)):
            st.markdown(message.parts[0].text)

    # Get user input
    user_prompt = st.chat_input("Ask Hamza")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        response = st.session_state.chat_session.send_message(
            user_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=200,
                temperature=0.3
            )
        )
        with st.chat_message("assistant"):
            st.markdown(response.text)
if __name__ == '__main__':
     main()