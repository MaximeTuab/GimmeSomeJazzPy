import numpy as np
import streamlit as st
import base64
from GimmeSomeJazz import GimmeSomeJazz
from GimmeSomeJazzGifs import GimmeSomeJazzGifs


DATASET = 'dataset/library.json'


def display_pdf(filename):
    with open(filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


def main():    
    gifer = GimmeSomeJazzGifs("LIVDSRZULELA")
    trainer = GimmeSomeJazz(DATASET)

    st.set_page_config(  # Alternate names: setup_page, page, layout
        layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        page_title="Gimme Somme Jazz!",  # String or None. Strings get appended with "• Streamlit". 
        page_icon="gsj-icon.png",  # String, anything supported by st.image, or None.
    )
    left_column, right_column = st.beta_columns(2)
    left_column.write("""
    # I'm your jazz coach
    Feeding you with the best of jazz
    """)
    button = left_column.button("Gimme some jazz!", "new")
    if button:
        desc = trainer.draw()
        gif = gifer.draw()
        left_column.write(desc)
        right_column.image(gif, width=400)
        right_column.write(gif)


def main_debug():
    trainer = GimmeSomeJazz(DATASET)
    while(True):
        desc, pdf = trainer.draw()


if __name__ == '__main__':
    main()
