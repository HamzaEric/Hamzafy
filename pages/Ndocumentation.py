import streamlit as st


def main():
    st.set_page_config(layout="wide")
    st.title('🛠️📖 Hamzafy AI Docs')
    st.info('# Your Personalized AI Chat Companion')
    st.markdown('---')
    st.title('❓ Why Use Hamzafy?')
    st.write('''
    Hamzafy is an AI chatbot built to have conversations with users in a friendly 
    and helpful way.
    Hamzafy can answer questions, tell jokes, motivate users, and chat casually.
    It is lightweight, easy to use, and does not need any complex setup.
    Just send a message, and Hamzafy will reply instantly.
    ''')

    st.write('##### Hamzafy is designed to make talking to AI simple, fast, and fun.')
    st.markdown('---')
    st.header("Development and API")
    st.write('You first import the necessary tools in your local environment')
    st.code('''
    import streamlit as st
    import google.generativeai as genai
    ''')
    st.write('Define a function to set the page layout')
    st.code('''
    def main():
    st.set_page_config(layout="wide")
      #whole code here#
    if __name__ == '__main__':
     main()
    ''')
    st.write('Add a background image for the chatbot using css')
    st.code('''
    # Add background image with CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://i.imgur.com/t31klTW.jpeg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    ''')
    st.write('Add Content')
    st.code('''
    st.title("Hamzafy")
    st.markdown('---')
    col1, col2 = st.columns(2)
    with col1:
        st.image('hamzafy.jpg', width=400)
    with col2:
        st.title("🤖Ask Hamza!")
        st.header('🚀Hamzafied AI!')
        st.markdown('---')

    ''')
    st.write('load the api securely and configure gemini')
    st.code('''
    # Load API key securely from secrets.toml
    api_key = st.secrets["gemini_api_key"]

    # Configure Gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    ''')
    st.write('''
    Write the system instruction 
    and add a function to display roles,
    finally start a session injecting the instructions to it.Create the history displaying function
    ''')
    st.code(''' 
    system_instruction = ('define system instruction')
    
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
    
    ''')
    st.write('Get the User Input')
    st.code('''
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
    ''')
    st.subheader('🏗️Tech Stack')
    st.write('''

    1.Language: Python

    2.IDE: Pycharm Professional
    
    3.UI:Streamlit
    ''')

    st.markdown('---')
    st.subheader('✅ Conclusion')
    st.markdown('---')
    st.write('#### Hamzafy is a text generation AI PLatform')
    st.write('''
    The model demonstrates strong capabilities in text generation by producing coherent,
    contextually appropriate, and human-like responses.
    Its ability to understand input prompts, maintain conversational flow, 
    and adapt tone based on context makes it highly effective for various 
    natural language processing tasks.
    Overall, it offers a reliable solution for building smart, responsive, and engaging
    AI-driven applications.
    ''')
    st.markdown('---')

    st.subheader('👨‍💻 Developer Information')
    st.markdown('---')
    st.code('''
    st.write('Name:Eric Hamza Maina')
    ''')
    st.write('Access Me')
    col1, col2 = st.columns(2)
    with col1:
        st.image('instagram.jpg')
    with col2:
        st.markdown('# [hamza.aah_k1](https://www.instagram.com/hamza.aaah_k1/)')

    col1, col2 = st.columns(2)
    with col1:
        st.image('github.jpg')
    with col2:
        st.markdown('# [HamzaEric](https://github.com/HamzaEric)')






if __name__ == '__main__':
    main()