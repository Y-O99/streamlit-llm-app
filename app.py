import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from openai import OpenAI

# OpenAIのAPIキーを環境変数から取得
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEYが環境変数に設定されていません。")
    st.stop()


st.title("Streamlit webアプリ課題: LLM_Webアプリ")

st.write("##### 動作モード1: 健康に関するアドバイス")
st.write("入力フォームに相談内容を入力し、「実行」ボタンを押すことで助言が得られます。")
st.write("##### 動作モード2: 育児に関するアドバイス")
st.write("入力フォームに相談内容を入力し、「実行」ボタンを押すことで助言が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康相談", "育児相談"]
)

client = OpenAI(api_key=openai_api_key)

if selected_item == "健康相談":
    input_message = st.text_input(label="健康に関する相談内容を入力してください。")
else: # 育児相談
    input_message = st.text_input(label="育児に関する相談内容を入力してください。")

if st.button("実行"):
    st.divider()
    

if selected_item == "健康相談":
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"},
            {"role": "user", "content": input_message}
        ],
        temperature=0.5
    )
    st.write(completion.choices[0].message.content)

else: # 育児相談
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "あなたは育児に関するアドバイザーです。安全なアドバイスを提供してください。"},
            {"role": "user", "content": input_message}
            ],
        temperature=0.5
    )
    st.write(completion.choices[0].message.content)
    