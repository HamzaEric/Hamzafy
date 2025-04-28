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