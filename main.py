import streamlit as st

# Page Config
st.set_page_config(
    page_title="My Awesome Website",
    page_icon="🌐",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌐 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# HOME PAGE
if page == "Home":
    st.title("Welcome to My Website 🚀")
    st.write("This is a modern website built using Streamlit!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🔥 Fast Performance</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🎨 Beautiful Design</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">⚡ Easy to Build</div>', unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f", use_container_width=True)

# ABOUT PAGE
elif page == "About":
    st.title("About Me 👨‍💻")
    st.write("""
    Hello! My name is Zain 👋  
    I am a Python developer and I love building websites using Streamlit.
    """)

    st.progress(80)

    st.subheader("Skills")
    st.write("- Python 🐍")
    st.write("- Web Development 🌐")
    st.write("- Streamlit ⚡")

# CONTACT PAGE
elif page == "Contact":
    st.title("Contact Me 📩")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.error("Please fill all fields ❌")