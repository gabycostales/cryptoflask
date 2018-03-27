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

// Polarites for sentiment line chart
let polarties = '{{ polarites }}';
console.log(polarities);

// Sentiment Line Chart
var ctx = document.getElementById("lineChart");
var lineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: weekdayLabels,
    datasets: [{
      label: 'Sentiment',
      data: [4, 5, 3, 6, 2, 7, 8],
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
          beginAtZero: true
        }
      }]
    }
  }
});


