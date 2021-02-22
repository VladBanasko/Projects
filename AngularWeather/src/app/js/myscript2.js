/* myscript2.js */
$(document).ready(function () {
    var d = new Date();
    $("#cdate").html(d);

    // Get data from Local Storage
    rowID = localStorage.getItem("rowID");
    cityArray = JSON.parse(localStorage.getItem("cityArray"));
    latArray = JSON.parse(localStorage.getItem("latArray"));
    lngArray = JSON.parse(localStorage.getItem("lngArray"));


    // Set latitude and longitude for selected city

    lat = latArray[rowID];
    lon = lngArray[rowID];


    // Get API key from https://home.openweathermap.org/

    // Build api string
    var apiURI = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=484e47e5a69dfcd6d1d089e84051d0d5`;

    // Get JSON data from remote server and display data

    $.ajax({
        type: 'GET',
        url: apiURI,
        dataType: 'jsonp',
        success: function (response) {
            console.log(response);
            $(".dataCity").html(response.name);
            $(".dataTemp").html((response.main.temp - 273.15).toFixed(2) + "C");
            $(".dataWind").html(response.wind.speed + " knots");
            $(".dataHum").html(response.main.humidity + " %");
            $(".dataPress").html(response.main.pressure + " mm");



        }

    });


});

/*
 The Kelvin scale is an absolute, thermodynamic temperature scale
 using as its null point absolute zero, the temperature at which
 all thermal motion ceases in the classical description of thermodynamics.
  To get Celsius, subtract 273.15 from Kelvin temp
*/