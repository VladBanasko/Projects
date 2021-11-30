
var countryName;
var background;
var pList = new Array();
var rowID;

class Prov {
    constructor(name, type, capital, flag, ...cities) {
        this.name = name;
        this.type = type;
        this.capital = capital;
        this.flag = flag;
        this.cities = cities;
    }
}

// document.ready statement
$(document).ready(function () {
    console.log('inside doc ready');
    $.ajax({
        type: "GET",
        dataType: "json",
        url: "/assets/dataFiles/canada.json",
        //url:"http://username.dev.fast.sheridanc.on,ca/DataFiles/canada.json"
        success: loadJSON,
        error: function (e) { alert(`${e.status} - ${e.statusTEst}`); }
    }); //end of ajax

    $("#backHead").click(function () { $("#background").toggle(); });

}); //end of doc ready


// loadJSON function
function loadJSON(data) {
    console.log("inside loadJSON");
    console.log(data);

    countryName = data.country.name;
    background = data.country.background;
    //load arrays
    for (let prov of data.country.division) {
        //prov = data.country.division[index]
        if (prov.type === 'province') {
            var cities = new Array();
            for (let city of prov.city) {
                cities.push(city);
            }

            pList.push(new Prov(prov.name, prov.type, prov.capital, prov.pic, cities));

        }
    } // end of for loop

    console.log(pList);

    //dispaly page
    mainScreen();
}


// mainScreen function
function mainScreen() {
    console.log("inside mainScreen");
    $("#country").html(`${countryName} - Provinces only`);
    $("#background").html(background);
    $("#background").hide();


    $("#provList").html("");

    for (x = 0; x < pList.length; x++) {
        $("#provList").append(
            `
	<li id='${x}'>
	<a href="otherPages/provPage.html">${pList[x].name}</a>


	 </li>
	`
        );
    }
}



// Save data to local storage
$(document).on("click", "#provList >li", function () {
    localStorage.setItem("countryName", countryName);
    localStorage.setItem("rowID", $(this).closest("li").attr("id"));
    localStorage.setItem("pList", JSON.stringify(pList));

});