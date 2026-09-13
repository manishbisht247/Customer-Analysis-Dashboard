import streamlit as st
from database import connect
from queries import get_customers
import pandas as pd
st.set_page_config(page_title = 'Customer Dashboard', layout = 'wide')

st.title('Customer Analytics Dashboard')


# connection
connection = connect()

if connection:
    cursor = connection.cursor(buffered = True)

    # filters

    st.sidebar.header('Filters')

    # selectbox country
    cursor.execute('select distinct country from customers')
    countries = [row[0] for row in cursor.fetchall()]
    country = st.sidebar.selectbox('country', countries + ['All'])

    # selectbox gender

    gender = st.sidebar.selectbox('gender', ['All', 'Male', 'Female'])

    # age range

    age = st.sidebar.slider('Age', min_value = 18, max_value = 100, value = (18, 100))

    # converting all into None

    selected_country = None if country == 'All' else country
    selected_gender = None if gender == 'All' else gender
    min_age = age[0]
    max_age = age[1]


    filtered_customers = get_customers(cursor, selected_country, selected_gender, min_age, max_age)
    df = pd.DataFrame(filtered_customers, columns = cursor.column_names)
    country_counts = df['country'].value_counts()
    st.bar_chart(country_counts)
    st.subheader('Filtered Customers')

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric('total customers', len(df))
    col2.metric('Average age', round(df['age'].mean(), 1))
    col3.metric('total countries', df['country'].nunique())

    st.dataframe(filtered_customers)

    gender_counts = df['gender'].value_counts()
    st.subheader('Gender')
    st.bar_chart(gender_counts)

    cursor.close()
    connection.close()
