import streamlit as st

st.write("こんにちは")

# テキスト(マークダウンで書けます。)
st.write("# title")

# 注釈
st.caption("注釈")

# 画像
st.image("https://ul.h3z.jp/tbfgZLSX.webp")

# テーブル
import pandas as pd
df = pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
st.write(df)

# チャート
st.line_chart(df)

# その他にもmatplotlib,altair,vega_lite,plotly,bokeh,,graphvizあたりを利用するAPIがあります。

# テキスト入力
name = st.text_input("名前")

# 数値入力
age = st.number_input("年齢",step=1)

st.write(f"名前: {name}")
st.write(f"年齢: {age}")

## ボタン
if st.button("Push"):
    st.write("ボタンを押しました")

# プルダウン
select = st.selectbox("好きな果物",options=["りんご","ばなな","いちご"])
st.write(select)

# プルダウン(複数選択)
multi_select = st.multiselect("好きな色",options=["赤","青","黄"])
st.write(multi_select)

# チェックボックス
check = st.checkbox("OK")
st.write(f"チェック：{check}")

# ラジオボタン
radio = st.radio("選択", ["猫", "犬"])
st.write(f"ラジオ：{radio}")

# ファイルアップロード
uploaded_file=st.file_uploader("Upload",type=["csv"])
if uploaded_file:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

st.write("# チャットbot")
# 定数定義
USER_NAME = "user"
ASSISTANT_NAME = "assistant"
MORIAGE_YAKU_NAME = "moriage_yaku"

# チャットログを保存したセッション情報を初期化
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# ユーザーのアバターを設定
avator_img_dict = {
    MORIAGE_YAKU_NAME: "🎉",
}

user_msg = st.chat_input("ここにメッセージを入力")
if user_msg:
    # 以前のチャットログを表示
    for chat in st.session_state.chat_log:
        avator = avator_img_dict.get(chat["name"], None)
        with st.chat_message(chat["name"], avatar=avator):
            st.write(chat["msg"])

    # 最新のメッセージを表示
    assistant_msg = "もう一度入力してください"
    moriage_yaku_msg = "アンコール！アンコール！"
    with st.chat_message(USER_NAME):
        st.write(user_msg)
    with st.chat_message(ASSISTANT_NAME):
        st.write(assistant_msg)
    with st.chat_message(MORIAGE_YAKU_NAME, avatar=avator_img_dict[MORIAGE_YAKU_NAME]):
        st.write(moriage_yaku_msg)

    # セッションにチャットログを追加
    st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
    st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": user_msg})
    st.session_state.chat_log.append({"name": MORIAGE_YAKU_NAME, "msg": user_msg})