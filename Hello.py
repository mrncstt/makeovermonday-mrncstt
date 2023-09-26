
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Make Over Moday",
        page_icon="📊",
    )

    st.write("# Make Over Moday 📊")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Makeover Monday is a weekly data visualization challenge where participants are provided with a dataset and an original visualization. 
        
        The goal is to improve or "makeover" the visualization by reimagining, redesigning, or simply tweaking it. 
       
         This initiative, led by the data community, aims to enhance data visualization skills, foster creativity, and build a supportive learning environment. 
        Participants often share their creations on social media, particularly Twitter/X, using the hashtag #MakeoverMonday, encouraging feedback and collaboration.
        

        **👈 Select a week from the sidebar** to see some examples

                ### Want to learn more?
        - Check out [Make Over Monday](https://www.makeovermonday.co.uk/)
        - Check [#MakeOverMonday](https://twitter.com/hashtag/MakeoverMonday?src=hashtag_click)
    """
    )


if __name__ == "__main__":
    run()
