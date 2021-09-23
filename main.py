from os import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 入門')

st.write('プログレスバーの表示')
'Start'

latest_interaction = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interaction.text(f'Iteration{i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ミギカラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたのお趣味をおしえてください。')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は', text 
# 'コンディション', condition
# if st.checkbox('Show Image'):
 #   img = Image.open('sample.jpg')
 #   st.image(img, caption='Shacho',use_column_width=True)

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```


# """