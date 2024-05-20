import os
import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import mpld3
from collections import Counter
from datetime import datetime

class PlotGenerator:
    def __init__(self):
        self.diseased_patients_html=""
        self.histogram_html=""
        self.pie_chart_html=""
        self.temperature_disease_correlation_html=""
    
    def calculate_age(self, dob):
        today = datetime.today()
        dob = datetime.strptime(dob, '%Y-%m-%d')
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def create_diseased_patients_plot(self, diseased_count):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(range(1, len(diseased_count) + 1), diseased_count)
        ax.set_xlabel('Days')
        ax.set_ylabel('Number of Diseased Patients')
        ax.set_title('Diseased Patients Over Time')
        ax.grid(True)
        ax.set_xlim(1, len(diseased_count))
    
        interval = 30
        ax.set_xticks(np.arange(1, len(diseased_count) + 1, step=interval))
        ax.set_xticklabels([f'{i}-{i+interval-1}' for i in range(1, len(diseased_count) + 1, interval)])
    
        if len(diseased_count) > 1:
            min_y = min(diseased_count[1:])
            max_y = max(diseased_count[1:])
        else:
            min_y = min(diseased_count)
            max_y = max(diseased_count)
    
        ax.set_ylim(min_y * 0.9, max_y * 1.1)
    
        self.diseased_patients_html += mpld3.fig_to_html(fig)
        image_path = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'diseased_patients_plot.png')
        fig.savefig(image_path)

    def create_histogram(self, patients):
        ages = [self.calculate_age(patient.personal_data.DOB) for patient in patients]
        fig, ax = plt.subplots(figsize=(12, 6))
        n, bins, patches = ax.hist(ages, bins=range(min(ages), max(ages) + 2), color='blue', edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Number of Patients')
        ax.set_title('Age Distribution of Patients')
        ax.set_xticks(bins)
        ax.set_xticklabels([str(int(x)) for x in bins], rotation=45, ha='right')
        plt.tight_layout()

        self.histogram_html += mpld3.fig_to_html(fig)
        image_path = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'age_histogram.png')
        fig.savefig(image_path)

    def create_disease_distribution_pie_chart(self, patients):
        try:
            disease_counts = Counter(disease.nombre for patient in patients for disease in patient.diseases_contracted)
            if not disease_counts:
                raise ValueError("No diseases found among provided patients.")
            labels, sizes = zip(*disease_counts.items())
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            ax.set_title('Disease Distribution Among Patients')

            self.pie_chart_html += mpld3.fig_to_html(fig)
            image_path = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'disease_distribution_pie_chart.png')
            fig.savefig(image_path)
        except Exception as e:
            print(f"Error while creating pie chart: {str(e)}")
            raise


    def create_temperature_disease_correlation(self, temperature_data, diseased_count):

        coeficiente_correlacion, p_valor = spearmanr(temperature_data, diseased_count)

        fig, ax = plt.subplots()
        ax.scatter(temperature_data, diseased_count)
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Number of Diseased Patients')
        ax.set_title('Correlation between Temperature and Diseased Patients\nSpearman correlation coefficient: {:.2f}'.format(coeficiente_correlacion))
        ax.grid(True)

        self.temperature_disease_correlation_html += mpld3.fig_to_html(fig)
        image_path = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'temperature_disease_correlation.png')
        fig.savefig(image_path)


    def save_html_files(self):
        diseased_patients_filepath = os.path.join(os.path.dirname(__file__), 'templates', 'static', "diseased_patients_graph.html")
        with open(diseased_patients_filepath, 'w') as diseased_patients_file:
            diseased_patients_file.write(self.diseased_patients_html)

        histogram_filepath = os.path.join(os.path.dirname(__file__), 'templates', 'static', "patients_histogram.html")
        with open(histogram_filepath, 'w') as histogram_file:
            histogram_file.write(self.histogram_html)

        pie_chart_filepath = os.path.join(os.path.dirname(__file__), 'templates', 'static', "disease_distribution_pie_chart.html")
        with open(pie_chart_filepath, 'w') as pie_chart_file:
            pie_chart_file.write(self.pie_chart_html)

        season_correlation_filepath = os.path.join(os.path.dirname(__file__), 'templates', 'static', "temperature_disease_correlation.html")
        with open(season_correlation_filepath, 'w') as season_correlation_file:
            season_correlation_file.write(self.temperature_disease_correlation_html)
