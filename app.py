import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Fake News Detector")

st.title("📰 Fake News Detection System")
st.write("Enter a news article and check whether it is Fake or Real.")

news = st.text_area("Paste News Article Here")

if st.button("Predict"):

    news_vector = vectorizer.transform([news])

    prediction = model.predict(news_vector)
    confidence = model.predict_proba(news_vector)

    if prediction[0] == 0:
        st.error("🚨 Fake News")
    else:
        st.success("✅ Real News")

    st.write(
        f"Confidence: {max(confidence[0])*100:.2f}%"
    )