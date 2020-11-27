async function riyadh(){
    let name = await eel.get_weather_riyadh()();
    let country = await eel.get_weather_riyadh2()();
    let temp = await eel.get_weather_riyadh3()();
    let main = await eel.get_weather_riyadh4()();
    var div = document.getElementById("name");
    div.innerHTML = name
    var div = document.getElementById("country");
    div.innerHTML = country
    var div = document.getElementById("temp");
    div.innerHTML = temp
    var div = document.getElementById("main");
    div.innerHTML = main
}
async function dubai(){
    let name = await eel.get_weather_dubai()();
    let country = await eel.get_weather_dubai2()();
    let temp = await eel.get_weather_dubai3()();
    let main = await eel.get_weather_dubai4()();
    var div = document.getElementById("name");
    div.innerHTML = name
    var div = document.getElementById("country");
    div.innerHTML = country
    var div = document.getElementById("temp");
    div.innerHTML = temp
    var div = document.getElementById("main");
    div.innerHTML = main
}
async function jeddah(){
    let name = await eel.get_weather_jeddah()();
    let country = await eel.get_weather_jeddah2()();
    let temp = await eel.get_weather_jeddah3()();
    let main = await eel.get_weather_jeddah4()();
    var div = document.getElementById("name");
    div.innerHTML = name
    var div = document.getElementById("country");
    div.innerHTML = country
    var div = document.getElementById("temp");
    div.innerHTML = temp
    var div = document.getElementById("main");
    div.innerHTML = main
}
async function egypt(){
    let name = await eel.get_weather_egypt()();
    let country = await eel.get_weather_egypt2()();
    let temp = await eel.get_weather_egypt3()();
    let main = await eel.get_weather_egypt4()();
    var div = document.getElementById("name");
    div.innerHTML = name
    var div = document.getElementById("country");
    div.innerHTML = country
    var div = document.getElementById("temp");
    div.innerHTML = temp
    var div = document.getElementById("main");
    div.innerHTML = main
}