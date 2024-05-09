$(document).ready(function() {
    $('#startSimulation').click(function() {
        $.ajax({
            url: '/run_simulation',
            type: 'GET',
            success: function(response) {
                // Handle the response here
                console.log('Simulation started successfully.');
                console.log('Simulation Results:', response);

                // Display simulation results
                $('#simulationResults').text('Simulation Results:');
                for (var i = 0; i < response.grid.length; i++) {
                    $('#simulationResults').append('<div>Day ' + response.grid[i].day + ': Patients ' + response.grid[i].patients + '</div>');
                }

                // Display the plot
                $('#simulationResults').append('<img src="' + response.img + '" alt="Simulation Plot">');
            },
            error: function(error) {
                console.log('Error starting simulation:', error);
            }
        });
    });
});
