import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(
              page_title="Census visual of India",
              layout='wide'
              )
st.markdown("""
            <style>
            .stApp{
                background-color: #0f172a;
            }
            [data-testid="stSidebar"]{
                background-color: #1e293b
            }
            h1,h2,h3{
                color: #f8fafc !important;
            }
            </style>
            """,unsafe_allow_html=True)
@st.cache_data
def load_data():
   return pd.read_csv('CensusMin.csv')
df=load_data()


list_state=list(df['State'].unique())
list_state.insert(0,'Overall India')


st.sidebar.title('Census of India')
selected_state=st.sidebar.selectbox('Select a state',list_state)

colms=sorted(df.columns[5:])

primary=st.sidebar.selectbox("Select Primary Parameter",colms)
secondary=st.sidebar.selectbox("Select Secondary perameter",colms)

plot=st.sidebar.button('Plot Graph')


if plot:
    st.text('Size represent Primary perameter')
    st.text('Color represent secodary perameter')
    
    if selected_state=='Overall India':
           fig=px.scatter_mapb(df,
                                 lat='Latitude',
                                 lon='Longitude',
                                 size=primary,
                                 color=secondary,
                                 zoom=4,
                                 size_max=35,
                                 map_style='carto-darkmatter',
                                 width=1200,
                                 height=700,
                                 hover_name='District'
                                 )
           
           fig.update_layout(
               template='plotly_dark',
               paper_bgcolor='rgba(0,0,0,0)',
               plot_bgcolor='rgba(0,0,0,0)',
               
           )
           
           st.plotly_chart(fig,use_container_width=True)
           
           
    else:
        state_df=df[df['State']==selected_state]
        
        fig=px.scatter_map(
            state_df,
            lat='Latitude',
            lon='Longitude',
            size=primary,
            color=secondary,
            zoom=6,
            size_max=35,
            map_style='carto-darkmatter',
            width=1200,
            height=700,
            hover_name='District',
            
        )
        
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            
        )
        
        st.plotly_chart(fig,use_container_width=True)
