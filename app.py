import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Google Translator
translator = Translator() # will be used to perform text translations in the app.


def translate_text(text, target_lang):  #to which the text should be translated.
    """
    Translate the input text to the target language.
    """
    translation = translator.translate(text, dest=target_lang)  #dest parameter specifies the destination language code.


    return translation.text


def main():  #main logic  Streamlit aap including the layout and interactivity of the interface.
    # Set up the Streamlit app layout
    st.markdown("<h1 style='color: purple;'>**Language Translation App**</h1>", unsafe_allow_html=True)

    # User input for text to translate
    text_to_translate = st.text_area("Enter Text to Translate","")

    # Drop-down menu for selecting the target language
    target_language = st.selectbox(
        "Select Language to Translate To",
        list(LANGUAGES.values())
    )

    # Convert language name to language code
    target_lang_code = [key for key, value in LANGUAGES.items() if value == target_language][0] #to find the matching language
    # code and store it in target_lang_code.

    # Translate when button is pressed
    st.markdown("""
        <style>
            .stButton > button {
                background-color: #4CAF50;  /* Green background */
                color: white;               /* White text */
                font-size: 16px;            /* Font size */
                padding: 10px 20px;         /* Padding */
                border-radius: 5px;         /* Rounded corners */
                border: none;               /* Remove border */
                cursor: pointer;           /* Pointer cursor on hover */
            }

            .stButton > button:hover {
                background-color: #45a049;  /* Slightly darker green on hover */
            }
        </style>
        """, unsafe_allow_html=True)# for styling the text

    if st.button("Translate"):
        if text_to_translate:
            translated_text = translate_text(text_to_translate, target_lang_code)
            st.subheader(f"Translated Text ({target_language}):")
            st.write(translated_text)
            st.balloons()
        else:
            st.warning("Please enter some text to translate.")
            st.snow()



if __name__ == "__main__":
    main()
