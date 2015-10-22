/**
 * Created by McDaemon on 05.11.14.
 */

//<![CDATA[
function showHide() {
    var ele = document.getElementById("vorschau");
    var ele2 = document.getElementById("aktuell");
    var ele3 = document.getElementById("container");
    var ele4=document.getElementById("wetterdaten");
    if(ele.style.display == "block") {
            ele.style.display = "none";
            ele2.style.display = "block";
            ele3.style.display = "none";
            ele4.style.display = "none";
      }
    else {
        ele.style.display = "block";
        ele2.style.display = "none";
        ele3.style.display = "none";
        ele4.style.display = "none";
    }
}
function showLogin(){
    var ele= document.getElementById("container");
    var ele2= document.getElementById("vorschau");
    var ele3= document.getElementById("aktuell");
    if(ele.style.display == "block") {
        ele.style.display="none";
        ele2.style.display="none";
        ele3.style.display="block";
    }
    else {
        ele.style.display="block";
        ele2.style.display="none";
        ele3.style.display="none";
    }
}

function showLoginEmber(){
    var ele= document.getElementById("containerEmber");
    var ele2=document.getElementById("wetterdaten");
    if(ele.style.display == "block") {
        ele.style.display="none";
        ele2.style.display="block";
    }
    else {
        ele.style.display="block";
        ele2.style.display="none";
    }
}

function showWeathers(){
    var ele=document.getElementById("wetterdaten");
    var ele2=document.getElementById("vorschau");
    var ele3=document.getElementById("aktuell");
    var ele4=document.getElementById("container");
    var ele5=document.getElementById("powered");
    if(ele.style.display == "block") {
        ele.style.display="none";
        ele2.style.display="none";
        ele3.style.display="block";
        ele4.style.display="none";
        ele5.style.display="block";

    }
    else{
        ele.style.display="block";
        ele2.style.display="none";
        ele3.style.display="none";
        ele4.style.display="none";
        ele5.style.display="none";
    }
}

function showComment(){
    var ele=document.getElementById("commentForm");
    if(ele.style.display == "block")
        ele.style.display = "none";
    else
        ele.style.display = "block";
}


function showAktuell(){
    var ele=document.getElementById("aktuell");
    var ele2=document.getElementById("vorschau");
    var ele3=document.getElementById("container");
    var ele4=document.getElementById("wetterdaten");
    ele.style.display="block";
    ele2.style.display="none";
    ele3.style.display="none";
    ele4.style.display="none";
}
function logout(){
    window.location.href="/accounts/logout/";
    return false;
    }
function register(){
    window.location.href="/accounts/signup/"
}


function ausgabe(){
        var datum = document.getElementById("datetimepicker2").value
        var city = document.getElementById('CityInputFeld').value
        window.location.href="/weathers/?search=" + datum + " " + city
}

// ]]>
