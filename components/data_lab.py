import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def create_dataset():

    np.random.seed(42)

    data = {
        "Study Hours": np.random.randint(1, 10, 100),
        "Social Media Hours": np.random.uniform(1, 8, 100),
        "Sleep Hours": np.random.uniform(4, 9, 100),
        "Academic Score": np.random.randint(40, 100, 100)
    }

    return pd.DataFrame(data)

def data_lab_section():

    st.markdown(
        """
        <h2>
            DATA <span class="accent">LAB</span>
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Explore data through interactive visualizations."
    )

    df = create_dataset()

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "X AXIS",
            df.columns
        )

    with col2:

        y_axis = st.selectbox(
            "Y AXIS",
            df.columns,
            index=1
        )

    analysis = st.selectbox(
        "VISUALIZATION",
        [
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Correlation"
        ]
    )

    if st.button("RUN ANALYSIS →"):

        if analysis == "Scatter Plot":

            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                title=f"{x_axis} vs {y_axis}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif analysis == "Histogram":

            fig = px.histogram(
                df,
                x=x_axis,
                title=f"Distribution of {x_axis}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif analysis == "Box Plot":

            fig = px.box(
                df,
                y=x_axis,
                title=f"Distribution of {x_axis}"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        elif analysis == "Correlation":

            corr = df.corr(numeric_only=True)

            fig = px.imshow(
                corr,
                text_auto=True,
                title="Correlation Matrix"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )