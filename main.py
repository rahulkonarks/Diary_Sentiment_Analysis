import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
positivity = []
negativity = []
filepaths = sorted(glob.glob('diary/*.txt'))
dates = [filepath.strip('.txt').strip('diary/') for filepath in filepaths]

for filename in filepaths:
    with open(filename, 'r') as file:
        diary_content = file.read()

    negativity.append(analyzer.polarity_scores(diary_content)['neg'])
    positivity.append(analyzer.polarity_scores(diary_content)['pos'])

pos_figure = px.line(x=dates, y=positivity, labels={'x': 'Date', 'y': 'Positivity'})
neg_figure = px.line(x=dates, y=negativity, labels={'x': 'Date', 'y': 'Negativity'})

st.title('Diary Tone')
st.subheader('Positivity')
st.plotly_chart(pos_figure)

st.subheader('Negativity')
st.plotly_chart(neg_figure)
