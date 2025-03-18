import pandas as pd
import streamlit as st
from model import plot_temperature


def process_main_page():
    show_main_page()
    process_side_bar_inputs()


def show_main_page():

    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Temperature Analyze",

    )

    st.write(
        """
        Анализ температурных данных и мониторинг текущей температуры
        """
    )

def process_side_bar_inputs():
    st.sidebar.header('Выберите город для анализа температуры')
    user_input_df = sidebar_input_features()

    train_df = plot_temperature(user_input_df["city"])


def sidebar_input_features():
    city = st.sidebar.selectbox("Город", ("New York", "London","Paris","Tokyo","Moscow","Sydney","Berlin","Beijing","Rio de Janeiro","Dubai","Los Angeles","Singapore","Mumbai","Cairo","Mexico City"))
    data = {
        "city": city
    }

    df = pd.DataFrame(data, index=[0])

    return df


if __name__ == "__main__":
    process_main_page()
