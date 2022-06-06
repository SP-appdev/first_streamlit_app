import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('❤Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeals')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-boiled Free-range Egg')
streamlit.text('🥑🍞Avocado toast')

streamlit.header('🍇🥝Build Your Own Fruit Smoothies🍌🥭')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

                      
streamlit.dataframe(my_fruit_list)
