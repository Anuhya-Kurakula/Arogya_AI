import streamlit as st


def load_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def show_examples():

    with st.expander("💡 Example Questions"):

        st.markdown("""

### 🌿 English

• What are symptoms of diabetes?

• What causes malaria?

• Calculate BMI for 70 kg and 1.75 m

• My BP is 150/95


### 🌿 Telugu

• డెంగ్యూ లక్షణాలు ఏమిటి?

• మధుమేహం లక్షణాలు ఏమిటి?


### 🌿 Hindi

• डायबिटीज के लक्षण क्या हैं?

• बुखार क्यों आता है?


### 🌿 Tamil

• காய்ச்சலின் அறிகுறிகள் என்ன?

""")