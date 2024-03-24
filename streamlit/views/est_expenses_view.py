import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

class EstExpensesView:
    """
    View class for rendering visualizations of estimated expenses.
    """

    @staticmethod
    def render_horizontal_bar_chart(fig):
        """
        Render a horizontal bar chart based on provided data.

        Args:
            fig (matplotlib.figure.Figure): The figure object containing the horizontal bar chart.

        Returns:
            matplotlib.figure.Figure: The rendered horizontal bar chart figure.
        """
        
        return fig

    @staticmethod
    def render_pie_chart(fig):
        """
        Render a pie chart based on provided data.

        Args:
            fig (matplotlib.figure.Figure): The figure object containing the pie chart.

        Returns:
            matplotlib.figure.Figure: The rendered pie chart figure.
        """
        fig, ax = plt.subplots(figsize=(6, 8))
        labels = list(data.keys())
        values = list(data.values())

        ax.pie(values, autopct='%1.1f%%', startangle=90)
        ax.set_title('Expenses Distribution')
        ax.legend(loc='center left', labels=labels, bbox_to_anchor=(1, 0, 0.5, 1), borderaxespad=1)
        st.pyplot(fig)
