import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from patient_data import PatientData
from ambiente import Ambiente
from enfermedad import Enfermedad
from pacientes_data import get_data
from plot import PlotGenerator
from mesa.time import RandomActivation
from mesa import Model
from mesa.space import MultiGrid

class PatientModel(Model):
    def __init__(self, pacientes_data):
        super().__init__()
        self.pacientes_data = pacientes_data
        self.grid_size = self.calculate_grid_size(len(pacientes_data['data']))
        self.grid = MultiGrid(self.grid_size, self.grid_size, torus=True)
        self.schedule = RandomActivation(self)
        self.patients = []

        # Initialize environment and possible diseases
        self.ambiente = Ambiente(1, self)
        self.possible_diseases = [
            Enfermedad("Flu", 0.1, ["Invierno", "Otoño"]),
            Enfermedad("Common cold", 0.1, ["Invierno", "Primavera"]),
            Enfermedad("COVID-19", 0.0206, ["Invierno", "Primavera", "Verano", "Otoño"])
        ]
        self.enfermos = []
        self.schedule.add(self.ambiente)
        self.load_all_patients()

    def calculate_grid_size(self, num_agents):
        size = math.ceil(math.sqrt(num_agents))
        while size ** 2 < num_agents:
            size += 1
        return size

    def load_all_patients(self):
        for pid in range(len(self.pacientes_data['data'])):
            patient = PatientData(self, self.pacientes_data, pid)  # Assuming PatientData class exists
            self.patients.append(patient)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(patient, (x, y))
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

        fig, ax = plt.subplots(figsize=(8, 8))
        im = ax.imshow([[0] * self.grid_size for _ in range(self.grid_size)], cmap='viridis', vmin=0, vmax=1)

        def update(day):
            self.step()
            temperaturas.append(self.ambiente.clima.temperature)
            diseased_count.append(len(self.enfermos))
            self.remove_cured_patients()

            # Update grid data for visualization based on sick_status of agents
            grid_data = [[0] * self.grid_size for _ in range(self.grid_size)]
            for cell in self.grid.coord_iter():
                x, y = cell[1]
                agents = self.grid.get_cell_list_contents([(x, y)])
                if agents:
                    # Check if any agent in this cell is sick
                    if any(agent.sick_status for agent in agents):
                        grid_data[y][x] = 1

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
