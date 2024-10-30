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

var InfectedPatientsModule = function(series, series_data) {
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    document.body.appendChild(canvas);

    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: series,
                data: [],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: false
        }
    });

    this.render = function(data) {
        chart.data.labels.push(data[0]);
        chart.data.datasets[0].data.push(data[1]);
        chart.update();
    };

    this.reset = function() {
        chart.data.labels = [];
        chart.data.datasets[0].data = [];
        chart.update();
    };
};
