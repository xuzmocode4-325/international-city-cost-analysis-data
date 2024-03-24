import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

class EstExpensesView:
    """
    View class for rendering visualizations of estimated expenses.
    """

    @staticmethod
    def render_horizontal_bar_chart(data):
        """
        Render a horizontal bar chart based on provided data.

        Args:
            data (dict): Dictionary containing expense categories as keys and their corresponding amounts as values.
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        keys = list(data.keys())
        values = list(data.values())
        y_pos = np.arange(len(keys))

        ax.barh(y_pos, values, align='center', alpha=0.5)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keys)
        ax.set_xlabel('Amount')
        ax.set_title('Expenses Breakdown')
        st.pyplot(fig)

    @staticmethod
    def render_pie_chart(data):
        """
        Render a pie chart based on provided data.

        Args:
            data (dict): Dictionary containing expense categories as keys and their corresponding amounts as values.
        """
        fig, ax = plt.subplots(figsize=(6, 8))
        labels = list(data.keys())
        values = list(data.values())

        ax.pie(values, autopct='%1.1f%%', startangle=90)
        ax.set_title('Expenses Distribution')
        ax.legend(loc='center left', labels=labels, bbox_to_anchor=(1, 0, 0.5, 1), borderaxespad=1)
        st.pyplot(fig)
