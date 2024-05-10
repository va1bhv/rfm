import warnings

import streamlit as st

warnings.filterwarnings("ignore")


def main() -> None:
    st.set_page_config(
        page_title="RFM Analysis",
        page_icon="🛍️",
        layout="wide",
        initial_sidebar_state="expanded")
    st.write('Hello, world!')


if __name__ == '__main__':
    main()
