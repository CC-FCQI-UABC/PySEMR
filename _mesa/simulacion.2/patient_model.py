import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mesa.time import RandomActivation
from mesa import Model
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import get_data
from plot import PlotGenerator

class PatientModel(Model):
    def __init__(self, pacientes_data):
        super().__init__()
        self.pacientes_data = pacientes_data
        self.schedule = RandomActivation(self)
        self.patients = []
        self.enfermos = []

        # Initialize environment and possible diseases
        self.ambiente = Ambiente(1, self)
        self.possible_diseases = [
            Enfermedad("Flu", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Common cold", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.0206, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        
        self.schedule.add(self.ambiente)
        self.load_all_patients()

    def load_all_patients(self):
        for pid in range(len(self.pacientes_data['data'])):
            patient = PatientData(self, self.pacientes_data, pid)
            self.patients.append(patient)
            self.schedule.add(patient)

    def step(self):
        self.ambiente.step()  # Simulate the change of season
        self.schedule.step()

    def remove_cured_patients(self):
        self.enfermos = [patient for patient in self.enfermos if patient.sick_status]

    def run_simulation(self, steps=365):
        plot_generator = PlotGenerator()
        diseased_count = []
        temperaturas = []

        # Calculate grid dimensions
        num_patients = len(self.patients)
        grid_size = math.ceil(math.sqrt(num_patients))
        
        fig, ax = plt.subplots(figsize=(6, 6))
        im = ax.imshow([[0] * grid_size for _ in range(grid_size)], cmap='viridis', vmin=0, vmax=1)

        def update(day):
            self.step()
            temperaturas.append(self.ambiente.clima.temperature)
            diseased_count.append(len(self.enfermos))
            self.remove_cured_patients()

            # Update data for visualization based on sick_status of agents
            grid_data = [[0] * grid_size for _ in range(grid_size)]
            for idx, patient in enumerate(self.patients):
                x = idx % grid_size
                y = idx // grid_size
                grid_data[y][x] = 1 if patient.sick_status else 0

            im.set_data(grid_data)
            ax.set_title(f"Day: {day}")
            plt.draw()

        anim = FuncAnimation(fig, update, frames=range(steps), repeat=False)
        plt.tight_layout()
        plt.show()

        # Plot static graphs after the simulation completes
        plot_generator.create_diseased_patients_plot(diseased_count)
        plot_generator.create_disease_distribution_pie_chart(self.enfermos)
        plot_generator.create_histogram(self.patients)
        plot_generator.create_temperature_disease_correlation(diseased_count, temperaturas)

        return self.patients, self.enfermos

# Example usage
if __name__ == "__main__":
    pacientes_data = get_data()  # Assuming get_data() function retrieves patient data
    model = PatientModel(pacientes_data)
    model.run_simulation(steps=365)
