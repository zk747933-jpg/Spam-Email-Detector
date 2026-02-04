import streamlit as st
import pickle

#LOAD MODEL AND TF-IDF
model = pickle.load(open('spam_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

#streamlit UI
st.title("Spam Email Detector")
st.write("Type or paste your email below to check if it's **Spam** or **Ham**.")

email_input = st.text_area("Enter your email content here: ")

if st.button("Predict"):
    if email_input.strip() !="":
        #Transform input text
        email_vector = tfidf.transform([email_input])

        #Predict
        prediction = model.predict(email_vector)[0]
        #show result
        if prediction == 1:
            st.error("⚠️ This email is SPAM!")
        else:
            st.success("✅ This email is (not spam).")
    else:
        st.warning("Please enter some text to check.")