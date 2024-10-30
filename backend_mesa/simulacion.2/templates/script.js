// ######################################################################
// ## PythonSyntheticElectronicMedicalRecords 1.0
// ## Modelo computacional de registros medicos electrónicos sintéticos 
// ## en Python.
// ######################################################################
// ## This software are distributed using the Creative Commons Public
// ## License "Attribution-NonCommercial-ShareAlike 4.0 International"
// ## https://creativecommons.org/licenses/by-nc-sa/4.0/
// ######################################################################
// ## Author: Manuel Castañón Puga, Claudio Emiliano Palacio Martínez, 
// ## Ricardo Fernando Rosales Cisneros, Carelia Guadalupe Gaxiola
// ## Pacheco, Luis Enrique Palafox Maestre.
// ## Copyright: Copyright 2024, Universidad Autónoma de Baja California.
// ######################################################################
// ## Credits: matplotlib, mesa, Flask, SQLAlchemy, Faker, requests, 
// ## tqdm, pandas and click libraries.
// ## License: CC BY-NC-SA 4.0
// ## Version: 1.0.0
// ## Mmaintainer: https://github.com/pugapuga.
// ## Email: puga@uabc.edu.mx
// ## Status: Released.
// ######################################################################

$(document).ready(function() {
    $('#startSimulation').click(function() {
        $.ajax({
            url: '/run_simulation',
            type: 'GET',
            success: function(response) {
                console.log('Simulation started successfully.');
                console.log('Simulation Results:', response);

                $('#simulationResults').text('Simulation Results:');
                for (var i = 0; i < response.grid.length; i++) {
                    $('#simulationResults').append('<div>Day ' + response.grid[i].day + ': Patients ' + response.grid[i].patients + '</div>');
                }

                $('#simulationResults').append('<img src="' + response.img + '" alt="Simulation Plot">');
            },
            error: function(error) {
                console.log('Error starting simulation:', error);
            }
        });
    });
});
