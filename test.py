import streamlit as st
from openai import OpenAI

# Настройка страницы
st.set_page_config(page_title="Исламский Помощник", layout="centered")

# Подключение к вашей Gemma в LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

st.title("🌙 Исламское обучение")

# Боковое меню (в Mini App оно будет сверху или выпадающим)
menu = ["Обучение", "Вопрос к ИИ", "Благотворительность"]
choice = st.sidebar.selectbox("Выберите раздел", menu)

if choice == "Обучение":
    st.header("📖 Ваши уроки")
    st.write("Здесь будут ваши материалы из Obsidian.")
    # Пример вывода урока
    with st.expander("Урок 1: Основы Таджвида"):
        st.write("Содержание урока...")

elif choice == "Вопрос к ИИ":
    st.header("🤖 Спросите Gemma")
    user_input = st.text_input("Ваш вопрос об Исламе:")
    
    if user_input:
        with st.spinner('Gemma думает...'):
            response = client.chat.completions.create(
                model="local-model",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices.message.content)

elif choice == "Благотворительность":
    st.header("🤝 Помощь и Садака")
    st.progress(65, text="Сбор на строительство медресе: 65%")
    if st.button("Пожертвовать"):
        st.success("Функция оплаты будет здесь!")


