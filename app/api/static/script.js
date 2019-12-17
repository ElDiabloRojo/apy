var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
    labels: years,
        datasets: [{
        label: "Africa",
        type: "line",
        borderColor: "#5ac18e",
            backgroundColorHover: "#ace0c6",
        data: africa,
        fill: false
    },{
        label: "Africa",
        type: "bar",
        backgroundColor: "#ff6666",
        backgroundColorHover: "#ffb2b2",
        data: africa
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