# plot.py
import os
import numpy as np
import matplotlib.pyplot as plt
import mpld3
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import *

class PlotGenerator:
    def __init__(self):
        self.diseased_patients_html = ""

    def create_diseased_patients_plot(self, diseased_count):
        # Plot the graph of diseased patients
        fig, ax = plt.subplots()
        # Start plotting from day 1, index 0 in the list
        ax.plot(range(1, len(diseased_count) + 1), diseased_count)  
        ax.set_xlabel('Days')
        ax.set_ylabel('Number of Diseased Patients')
        ax.set_title('Diseased Patients Over Time')
        ax.grid(True)
        ax.set_xlim(1, len(diseased_count))  # Adjust x-axis to start from day 1

        # Set y-axis limits more tightly around the data we care about
        if len(diseased_count) > 1:
            min_y = min(diseased_count[1:])  # Skip the first day if it's an outlier
            max_y = max(diseased_count[1:])
        else:
            min_y = min(diseased_count)
            max_y = max(diseased_count)

        ax.set_ylim(min_y * 0.9, max_y * 1.1)  # Give some padding around min and max

        # Convert the figure to HTML using mpld3
        self.diseased_patients_html += mpld3.fig_to_html(fig)

    def save_html_files(self, diseased_patients_filename):
        # Write the HTML content to files
        diseased_patients_filepath = os.path.join(os.path.dirname(__file__), 'templates', 'static', diseased_patients_filename)
        with open(diseased_patients_filepath, 'w') as diseased_patients_file:
            diseased_patients_file.write(self.diseased_patients_html)
