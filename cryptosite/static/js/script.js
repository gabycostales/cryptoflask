// Get Past 7 Weekdays for Sentiment X Axis
const weekdays = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
let weekdayLabels = [];
for (var i = 6; i >= 0; i--) {
  var d = new Date();
  d.setDate(d.getDate() - i);
  console.log(d.getDay());
  weekdayLabels.push(weekdays[d.getDay()]);
}
// console.log(weekdayLabels);


// Sentiment Line Chart
var ctx = document.getElementById("lineChart");
var lineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: weekdayLabels,
    datasets: [{
      label: 'Sentiment',
      data: polarities,
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 0.2)',
      borderWidth: 1
    }]
  },
  options: {
    legend: false,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false,
          scaleStartValue : -1,
          scaleSteps : .2
        }
      }]
    }
  }
});


