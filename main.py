import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Interration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
expander = st.expander('問い合わせ')
expander.write('問い合わせ1の回答')

text = st.text_input(
    'あなたの好きな趣味を教えてください',
)



condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの好きな趣味:',text
'コンディション：', condition

#if st.checkbox('Show Image'):
#    img = Image.open('DSC02972.JPG')
#    st.image(img, caption='元乃隅神社', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#    )
#st.map(df)