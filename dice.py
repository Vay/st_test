import streamlit as st
import random
import pandas as pd


def dice_once(dice_type):
    if dice_type == 'coin':
        return random.choice([0, 1])
    if dice_type == 'tetrahedron':
        return random.choice([0, 1, 2, 3])
    if dice_type == 'dice':
        return random.choice([0, 1, 2, 3, 4, 5])
    if dice_type == 'octahedron':
        return random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

def roll_once(dice_type, dice_count):
    result = []
    for i in range(dice_count):
        result.append(dice_once(dice_type))
    return result

def roll_many(dice_type, dice_count, rolls_count):
    result = []
    for i in range(rolls_count):
        result.append(roll_once(dice_type, dice_count))
    return result


dice_type = st.sidebar.selectbox('Type of dice', ('coin', 'tetrahedron', 'dice', 'octahedron'))
dice_count = st.sidebar.slider('How many dice?', 1, 10, 2)
rolls_count = st.sidebar.number_input('Rolls count', min_value=1, max_value=1000, value=5, step=1)

st.write('Hello world!')
st.write(dice_type, dice_count)
if st.sidebar.button('Roll!'):
    result = roll_many(dice_type, dice_count, rolls_count)
    df = pd.DataFrame(result)
    st.line_chart(df)
    st.bar_chart(df)
    df['sum'] = df.sum(axis=1)
    st.dataframe(df)
    st.bar_chart(df['sum'].value_counts())
