var cityArray = new Array();
var latArray = new Array();
var lngArray = new Array();
var rowID;

// Load data from JSON and save to Local Storage
$(document).ready(function () {

    $.getJSON("assets/dataFiles/cities.json", function (data) {
        console.log(data);


        $("#cityList").html("");

        for (let x = 0; x < data.cities.length; x++) {
            //build arrays
            cityArray[x] = data.cities[x].cityName;
            latArray[x] = data.cities[x].cityLat;
            lngArray[x] = data.cities[x].cityLng;

            // build <li>
            $("#cityList").append(
                `
                        <li id='${x}'>
                        <a href='assets/pages/weather.html'>${data.cities[x].cityName}</a>
                        </li>
                    `
            );
        }

        localStorage.setItem("cityArray", JSON.stringify(cityArray));
        localStorage.setItem("latArray", JSON.stringify(latArray));
        localStorage.setItem("lngArray", JSON.stringify(lngArray));
    }

    ); //end of doc ready
});


// Find the row selected and save to Local Storage

$(document).on("click", "#cityList >li", function () {

    localStorage.setItem("rowID", $(this).closest("li").attr("id"));

});