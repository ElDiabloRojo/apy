var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: "values",
            type: "line",
            backgroundColor: "#ff6666",
            backgroundColorHover: "#ffb2b2",
            data: values,
            fill: false
        },{
            label: "durations",
            type: "line",
            borderColor: "#5ac18e",
            backgroundColorHover: "#ace0c6",
            data: durations,
            fill: false
        },{
            label: "values",
            type: "bar",
            backgroundColor: "#ff6666",
            backgroundColorHover: "#ffb2b2",
            data: values
        },{
            label: "durations",
            type: "bar",
            borderColor: "#5ac18e",
            backgroundColorHover: "#ace0c6",
            data: durations
        }
        ]
},
    options: {
        title: {
            display: true,
                text: 'apy db stats'
        },
        legend: { display: false }
    }
});