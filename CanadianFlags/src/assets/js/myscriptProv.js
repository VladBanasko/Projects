// myscript for 03-AJAX-01-Canada using AJAX for individual pagevar countryName;
var pList = new Array();
var rowID;
var cList = new Array();

$(document).ready(function () {
    // get local storage values

    countryName = localStorage.getItem("countryName");
    pList = JSON.parse(localStorage.getItem("pList"));
    rowID = localStorage.getItem("rowID");
    // fill in output fields
    $("#country").html(countryName);
    $("#pname").html(pList[rowID].name);
    $("#capital").html(pList[rowID].capital);

    $("#flag").html(`<img src ='../images/${pList[rowID].flag}'>`);


    $("#cities").html("Major Cities<br>")
    $("#cities").css("text-align", "left");
    for (let city of pList[rowID].cities[0]) {
        $("#cities").append(`- ${city}<br>`);
    }


    /*
    for(x=0;x<pList[rowID].cities[0].length;x++){
        $("#cities").append(` -${pList[rowID].cities[0][x]<br>}`);
    } */

});