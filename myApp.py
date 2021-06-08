import streamlit as st
import numpy as np
import pandas as pd
import time
import json

st.title('Scrapbox')

st.header('Streamlitを触ってみた')

st.subheader('初めに')
st.write('Pythonのコーディングで少し調査していた時に')
'面白そうなフレームがあったので触ってみました。'  # st.writeは省略可

st.subheader('JSONデータの表示')
# アップローダー
json_file = st.file_uploader('JSONファイルをアップロード')
# json_fileがあるとき
if json_file is not None:
    # JSON表示
    st.json(json_file.getvalue().decode("utf-8"))


st.subheader('地図表示(本社)')
# 地図表示
df = pd.DataFrame(
    [[34.686158831221405, 135.18732456051012]],
    columns=['lat', 'lon']
)
st.map(df)

st.subheader('Magic commands')
# Magic commands
expander = st.beta_expander('マークダウン')
expander.write("""
# マークダウンでかける
## Scrapbox
### Streamlitを触ってみた
```python
import streamlit as st
import numpy as np
import pandas as pd
import time
import json

st.title('Scrapbox')

st.header('Streamlitを触ってみた')

st.subheader('初めに')
st.write('Pythonのコーディングで少し調査していた時に')
'面白そうなフレームがあったので触ってみました。'  # st.writeは省略可

st.subheader('JSONデータの表示')
# アップローダー
json_file = st.file_uploader('JSONファイルをアップロード')
# json_fileがあるとき
if json_file is not None:
    # JSON表示
    st.json(json_file.getvalue().decode("utf-8"))


st.subheader('地図表示')
# 地図表示
df = pd.DataFrame(
    [[34.686158831221405, 135.18732456051012]],
    columns=['lat', 'lon']
)
st.map(df)
```
""")














# left_side, right_side = st.beta_columns(2)
# button = left_side.button('表に変換')

# if button:
#     'hyouhouh'


# # グラフ、表
# st.write('DataFrame')
# df = pd.DataFrame({
#     '1列': [1, 2, 3, 4],
#     '2列': [11, 22, 33, 44]
# })

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('表示ボタン')
# if button:
#     right_column.write(df)

# expander = st.beta_expander('問い合わせ1')
# expander.write('記載箇所')

# expander = st.beta_expander('問い合わせ2')
# expander.write('記載箇所')

# expander = st.beta_expander('問い合わせ3')
# expander.write('記載箇所')

# st.dataframe(df.style.highlight_max(axis=0), width=300, height=200)
# st.table(df.style.highlight_max(axis=0))
# df2 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# # 折れ線グラフ
# # st.line_chart(df2)
# # エリアグラフ
# # st.area_chart(df2)
# # 棒グラフ
# st.bar_chart(df2)

# # インプット関係
# # API reference → Display interactive widgets
# df3 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df3)
# # API reference → Display interactive widgets
# st.sidebar.write('スライダー')
# slider = st.sidebar.slider('体温は？', 35, 40, 36)
# st.write('体温は「', slider, '」')

# st.sidebar.write('テキスト入力')
# text = st.sidebar.text_input('趣味は？')
# st.write('趣味は「', text, '」')

# st.write('セレクトボックス')
# option = st.selectbox(
#     '数字を入力',
#     list(range(1, 11))
# )
# st.write('入力した数字「', option, '」')

# st.write('チェックボックス')
# if st.checkbox('Show Image'):
#     # 画像表示
#     st.write('Display Image')
#     img = Image.open('image.png')
#     st.image(img, caption='test', use_column_width=True)
#     # use_column_width 実際のレイアウトの横幅に合わせて表示する
#     # API reference → Display media


