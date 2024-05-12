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
