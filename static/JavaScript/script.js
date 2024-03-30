

function renderMap(){
    var mapDiv = document.getElementById('map-image')

    var img = new Image()

    img.onload = function() 
    {
        imgDiv.innerHTML = ''
        imgDiv.appendChild(img)
    }
}
