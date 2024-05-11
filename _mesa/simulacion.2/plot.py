import matplotlib.pyplot as plt
import mpld3
import os

def create_plot(diseased_count):
    # Plot the graph of diseased patients
    fig, ax = plt.subplots()
    ax.plot(range(1, 366), diseased_count)
    ax.set_xlabel('Days')
    ax.set_ylabel('Number of Diseased Patients')
    ax.set_title('Diseased Patients Over Time')
    ax.grid(True)
    ax.set_xlim(0, 366)

    # Convert the figure to HTML using mpld3
    html_content = mpld3.fig_to_html(fig)

    # Write the HTML content to a file
    html_filename = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'diseased_patients_graph.html')
    with open(html_filename, 'w') as html_file:
        html_file.write(html_content)
