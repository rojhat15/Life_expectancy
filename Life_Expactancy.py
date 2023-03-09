#!/usr/bin/env python
# coding: utf-8

# # Installeren van alle benodigde packages

# In[1]:


#pip install kaggle


# In[2]:


from kaggle.api.kaggle_api_extended import KaggleApi


# In[3]:


api = KaggleApi()
api.authenticate()


# In[4]:


import zipfile


# In[5]:


import streamlit as st
import sklearn


# In[20]:


#pip install streamlit


# In[67]:


import pandas as pd
import plotly.express as px
from PIL import Image

# # Student performance prediction for beginner DATASET

# In[1]:


#!kaggle datasets download -d rkiattisak/student-performance-in-mathematics


# In[7]:


with zipfile.ZipFile("student-performance-in-mathematics.zip","r") as zip_ref:
    zip_ref.extractall()


# In[55]:


df = pd.read_csv("Student performance in mathematics.csv")


# # STREAMLIT Codes 

# In[45]:


HeaderImage = Image.open('Header.jpeg')
st.image(HeaderImage, width=290)


# In[19]:


st.header('Groep 2 Streamlit-app')


# In[47]:


st.markdown('Voor onze 2e casus hebben wij, Bodhian, Jasmijn, Yvette en Rojhat, de opdracht gekregen om data van een openbare API op te halen en deze te analyseren om hieruit interessante inzichten te delen. Wij ondersteunen ons verhaal dus met Streamlit en hebben een blog hiermee geschreven.')


# In[26]:


st.header('API')


# In[53]:


st.markdown('*In dit onderdeel zullen wij het ophalen van informatie via een openbare API behandelen*')


# In[36]:


st.markdown('Via Kaggle hebben wij de dataset: **Student performance prediction for beginner**, binnengehaald via een openbare API. Wij hebben eerst de Kaggle API naar onze laptop moeten downloaden en hebben vervolgens via een API-command de dataset gedownload.')


# In[39]:


st.markdown('Deze dataset bevat informatie over de prestaties van middelbare scholieren in wiskunde, inclusief hun cijfers en demografische informatie. De gegevens zijn verzameld van drie middelbare scholen in de Verenigde Staten.')


# In[48]:


st.markdown('De kolommen van de dataset zien er als volgt uit:')


# In[49]:


columnsimage = Image.open('columns.JPG')
st.image(columnsimage, caption='Kolom informatie')


# In[50]:


st.header('Data verkenning:')


# In[52]:


st.markdown('*In dit onderdeel zullen wij de data verkennen en waar nodig is zal er acties genomen worden om onnodige data te vermijden*')


# In[61]:


st.markdown('**De gehele dataset:**')
st.write(df)


# In[65]:


st.markdown('**Aantal rijen en kolommen:**')
st.write(df.shape)


# In[66]:


st.markdown('**.Describe() functie op de dataset**')
st.write(df.describe())


# In[134]:


st.markdown('**Aantal NaN-values:**')
st.write(df.isna().sum())


# In[]:

dfZonderId = df[['Math score', 'Reading score', 'Writing score']]

st.markdown('**Correlatie van de cijfers:**')
st.write(dfZonderId.corr())


# In[155]:


st.header('Data cleaning Race/ethnicity')


# In[157]:





st.markdown('De **Race/ethnicity kolom is onduidelijk.** Er valt niet te zien over welk afkomst het gaat, ook is dit niet in de documentatie te vinden. Daarom verwijderen wij deze kolom in onze nieuwe dataframe omdat er geen uitspraken over bepaalde afkomsten gedaan kunnen worden')
df2 = df.loc[:, df.columns != 'Race/ethnicity']


Knoppen = st.radio('Selecteer de afkomstgroep om aan te tonen:', ('Group A', 'Group B', 'Group C', 'Group D', 'Group E'))

if Knoppen == 'Group A':
    st.write(df[df['Race/ethnicity'] == 'Group A'])

if Knoppen == 'Group B':
    st.write(df[df['Race/ethnicity'] == 'Group B'])

if Knoppen == 'Group C':
    st.write(df[df['Race/ethnicity'] == 'Group C'])

if Knoppen == 'Group D':
    st.write(df[df['Race/ethnicity'] == 'Group D'])

if Knoppen == 'Group E':
    st.write(df[df['Race/ethnicity'] == 'Group E'])

# In[144]:


st.header('Persoonlijke data analyse:')


# In[149]:

st.write('Wijzig de plot in de **sidebar** naar eigen wensen')

global numeric_columns

numeric_columns = list(df2.select_dtypes(['object', 'float', 'int']).columns)
chart_select = st.sidebar.selectbox(label='Selecteer de grafiektype', options=['Scatterplot', 'Lineplot', 'Histogram', 'Boxplot'])


# In[150]:


if chart_select == 'Scatterplot':
    st.sidebar.subheader('Scatterplot selecties')
    x_values = st.sidebar.selectbox('X-as', options=numeric_columns)
    y_values = st.sidebar.selectbox('Y-as', options=numeric_columns)
    plot = px.scatter(data_frame=df2, x=x_values, y=y_values)
    st.plotly_chart(plot)

# In[ ]:

if chart_select == 'Lineplot':
    st.sidebar.subheader('Lineplot selecties')
    x_values = st.sidebar.selectbox('X-as', options=numeric_columns)
    y_values = st.sidebar.selectbox('Y-as', options=numeric_columns)
    plot2 = px.line(data_frame=df2, x=x_values, y=y_values)
    st.plotly_chart(plot2)

# In[ ]:

if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram selecties')
    x_values = st.sidebar.selectbox('X-as', options=numeric_columns)
    y_values = st.sidebar.selectbox('Y-as', options=numeric_columns)
    plot3 = px.histogram(data_frame=df2, x=x_values, y=y_values)
    st.plotly_chart(plot3)


# In[ ]:

if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot selecties')
    x_values = st.sidebar.selectbox('X-as', options=numeric_columns)
    y_values = st.sidebar.selectbox('Y-as', options=numeric_columns)
    plot4 = px.box(data_frame=df2, x=x_values, y=y_values)
    st.plotly_chart(plot4)

# In[151]:


st.header('Data analyse')


# In[ ]:

st.write('**De verschillende scores door de studenten behaald:**')

TrendlineButtons = st.radio('Met of zonder trendline:', ('Zonder trendline', 'Met trendline'))

figuur1 = px.scatter(df2, x=['Math score', 'Reading score','Writing score'], y='Student ID')

if TrendlineButtons == 'Zonder trendline':
    st.plotly_chart(figuur1)

if TrendlineButtons == 'Met trendline':
    figuur1 = px.scatter(df2, x=['Math score', 'Reading score','Writing score'], y='Student ID', trendline='ols')
    st.plotly_chart(figuur1)



# In[ ]:

st.header('Voorspellende modellen')

st.markdown('')
