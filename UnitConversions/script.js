function temperature() {
    //Temp(Fahrenheit) = [Temp(Degrees)*9/5] + 32
    var c = document.getElementById("celsius").value;
    var f = (c * 9 / 5) + 32;
    document.getElementById("fahrenheit").value = f;
}

function weight() {
    //Weight(Pounds) = Weight(Kgs) * 2.2
    var kg = document.getElementById("kilo").value;
    var p = kg * 2.2
    document.getElementById("pounds").value = p
}

function distance() {
    //Distance(Miles) = Distance(Kms) * 0.62137
    var km = document.getElementById("km").value;
    var m = km * 0.62137
    document.getElementById("miles").value = m

}