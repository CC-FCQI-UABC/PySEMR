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
