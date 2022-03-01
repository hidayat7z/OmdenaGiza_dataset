import pandas as pd
import streamlit as st
import plotly.express as px

df= pd.read_csv('https://raw.githubusercontent.com/hidayat7z/OmdenaGiza_dataset/main/USD_GBP_EURvs_EgyptianCurrency_from_2016_to_2022.csv')
df= df.iloc[:,1:8]

dollars= df[df['Type']=='USD']
pounds= df[df['Type']=='GBP']
euros= df[df['Type']=='EUR']

option = st.selectbox('Select Currency',('Select','US Dollars vs Egyptian Pound', 'Pound Sterling vs Egyptian Pound', 'Euro vs Egyptian Pound'))

if option == 'Select':
    fig = px.line(df, x="Date", y="Close", color='Type')
    st.plotly_chart(fig)
    st.write('The GBP curve has always been above than EUR and the EUR curve has always been above than USD except for a short period in 2017. \n\nWe can see that in November 2016 there was a sizeable rise in the exchange rates of USD, GBP and EUR against EGP. This is because on Novemeber 3, 2016 Central Bank of Egypt devalued its currency by 48% and announced that it will be allowed to float – measures that meet a key demand by the International Monetary Fund in order to secure a $12bn (£9.6bn) loan over three years to overhaul its ailing economy. Read more here: https://www.theguardian.com/world/2016/nov/03/egypt-devalues-currency-meet-imf-demands-loan\n\n In March 2018, exchange rates of USD, GBP and EUR against EGP reached their lowest value in around three and a half years demonstrating that the economy was gathering momentum following a series of IMF-induced reforms that began in November 2016 with the floating of the pound. Read more here: https://www.focus-economics.com/countries/egypt/news/gdp/economy-continues-gathering-pace-in-the-january-march-period\n\n As of February 2022 our data indicates the exchange rates of EUR/EGP and GBP/EGP have been in a downtrend for the past 1 year whereas in the case USD/EGP is 15.719 the rate has been constant for around a year.')
    st.caption('The dataset contains daily values of Open, High, Low, Close and Adj Close of the currency exchange rates of US Dollar, Pound Sterling and Euro against Egyptian Pound from 2016-02-22 to 2022-02-22. The data was gathered from the website of Yahoo! Finance.')

if option == 'US Dollars vs Egyptian Pound':
    fig = px.line(dollars, x='Date', y="Close")
    fig.update_layout(width=940, height=500)
    st.caption('Currency exchange rate of US Dollars vs Egyptian Pound')
    st.plotly_chart(fig)
    fig2 = px.histogram(dollars, x="Close")
    st.plotly_chart(fig2)
    st.markdown('In the past 6 years the exchange rate of USD against EGP has mostly been in the region of 15.5 to 18.5.The missing values from 9.5 to 15 is due to the devaluation of Egyptian currency in November 2016 as mentioned before.')

if option == 'Pound Sterling vs Egyptian Pound':
    fig = px.line(pounds, x='Date', y="Close")
    fig.update_layout(width=940, height=500)
    st.caption('Currency exchange rate of Pound Sterling vs Egyptian Pound')
    st.plotly_chart(fig)
    fig2 = px.histogram(pounds, x="Close")
    st.plotly_chart(fig2)
    st.markdown('In the past 6 years the exchange rate of GBP against EGP has mostly been in the region of 19 to 25. The missing values from 13.5 to 17.5 is due to the devaluation of Egyptian currency in November 2016 as mentioned before.')

if option == 'Euro vs Egyptian Pound':
    fig = px.line(euros, x='Date', y="Close")
    fig.update_layout(width=940, height=500)
    st.caption('Currency exchange rate of Euro vs Egyptian Pound')
    st.plotly_chart(fig)
    fig2 = px.histogram(euros, x="Close")
    st.plotly_chart(fig2)
    st.markdown('In the past 6 years the exchange rate of EUR against EGP has mostly been in the region of 16.5 to 22. The missing values from 10.5 to 16.5 is due to the devaluation of Egyptian currency in November 2016 as mentioned before.')