
var tData = function() {
  return Math.round(Math.random() * 25) + 10
};

var hData = function() {
  return Math.round(Math.random() * 50) + 10
};

var vData = function() {
  return Math.round(Math.random() * 1000) + 10
};

var lData = function() {
  return Math.round(Math.random() * 500) + 10
};


var tbarChartData = {
  labels: ["Sec1", "Sec2", "Sec3", "Sec4", "Sec5", "Sec6", "Sec7", "Sec8", "Sec9", "Sec10"],
  datasets: [{
    fillColor: "rgba(0,60,100,1)",
    strokeColor: "red",
    data: [tData(), tData(), tData(), tData(), tData(), tData(), tData(), tData(), tData(), tData()]
  }]
}

var hbarChartData = {
  labels: ["Sec1", "Sec2", "Sec3", "Sec4", "Sec5", "Sec6", "Sec7", "Sec8", "Sec9", "Sec10"],
  datasets: [{
    fillColor: "rgba(0,60,100,1)",
    strokeColor: "red",
    data: [hData(), hData(), hData(), hData(), hData(), hData(), hData(), hData(), hData(), hData()]
  }]
}

var vbarChartData = {
  labels: ["Sec1", "Sec2", "Sec3", "Sec4", "Sec5", "Sec6", "Sec7", "Sec8", "Sec9", "Sec10"],
  datasets: [{
    fillColor: "rgba(0,60,100,1)",
    strokeColor: "red",
    data: [vData(), vData(), vData(), vData(), vData(), vData(), vData(), vData(), vData(), vData()]
  }]
}
var lbarChartData = {
  labels: ["Sec1", "Sec2", "Sec3", "Sec4", "Sec5", "Sec6", "Sec7", "Sec8", "Sec9", "Sec10"],
  datasets: [{
    fillColor: "rgba(0,60,100,1)",
    strokeColor: "red",
    data: [lData(), lData(), lData(), lData(), lData(), lData(), lData(), lData(), lData(), lData()]
  }]
}


var index = 11;

var ctx = document.getElementById("canvas").getContext("2d");
var barChartDemo = new Chart(ctx).Bar(tbarChartData, {
  responsive: true,
  barValueSpacing: 3
});

var ctx2 = document.getElementById("canvas2").getContext("2d");
var barChartDemo2 = new Chart(ctx2).Bar(hbarChartData, {
  responsive: true,
  barValueSpacing: 4
});

setInterval(function() {
  barChartDemo.removeData();
  barChartDemo.addData([tData()], "Sec " + index);
  barChartDemo2.removeData();
  barChartDemo2.addData([hData()], "Sec " + index);

  index++;
}, 2000);
/*
setInterval(function(){
  $.get('/Room A', function(data, status){
          //console.log(data);
          $('#currentLoc').text("Now at: "+data);
      });
  $.get('/Room B', function(data, status){
          //console.log(data);
          $('#currentState').text(data);
      });
  $.get('/Room C', function(data, status){
          //console.log(data);
          $('#currentDest').text(data);
      });
}, 1000)
*/







/*
setInterval(function() {

  barChartDemo3.removeData();
  barChartDemo3.addData([vData()], "Sec " + index);
  barChartDemo4.removeData();
  barChartDemo4.addData([lData()], "Sec " + index);
  index++;
}, 2000);
*/
