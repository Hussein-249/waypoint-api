// importing jQuery
//import $ from "https://code.jquery.com/jquery-3.6.0.min.js";

var additionalWaypoints = 1

function initializeMap() {
    // setting the map in the 'leaflet-map' div, default focus on Toronto
    var map = L.map('leaflet-map').setView([43.65, -79.35], 9);

    // tile layer must be specified, else blank map
    L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.opentopomap.org/copyright">OpenTopoMap</a>'
    }).addTo(map);
}


function dynamicAddWaypointDiv() {

    var addWayPointButton = document.getElementById('add-button');
    var form = document.getElementById('add-waypoint-section');
    //    var form = document.querySelector('form');

    addWayPointButton.addEventListener('click', function() {

    if (additionalWaypoints == 4)
    {
        removeTargetInput = document.getElementById('waypoint-nr-' + additionalWaypoints)
        removeTargetLabel = document.getElementById('waypoint-label-' + additionalWaypoints)

        form.removeChild(removeTargetInput);
        form.removeChild(removeTargetLabel);

        additionalWaypoints--;

        return;
    }


        if (additionalWaypoints == 3)
        {
//            addWayPointButton.style.display = 'none';
            addWayPointButton.innerHTML = 'Remove Waypoints';

        }

        additionalWaypoints++;

        var waypointInput = document.createElement('input');
        waypointInput.setAttribute('type', 'text');
        waypointInput.setAttribute('id', 'waypoint-nr-' + additionalWaypoints);
        waypointInput.setAttribute('name', 'waypoint-nr-' + additionalWaypoints);

        var waypointLabel = document.createElement('label');
        waypointLabel.setAttribute('for', 'waypoint-nr-' + additionalWaypoints);
        waypointLabel.setAttribute('id', 'waypoint-label-' + additionalWaypoints);
        waypointLabel.textContent = 'Point ' + additionalWaypoints;

        if (additionalWaypoints >= 3)
        {
            form.appendChild(document.createElement('br'));
        }
        form.appendChild(waypointLabel);
        form.appendChild(document.createElement('br'));
        form.appendChild(waypointInput);
    });
}


function removeWaypointDiv() {
    var removeWayPointButton = document.getElementById('remove-button');
    var form = document.getElementById('add-waypoint-section');

//    if (additionalWaypoints > 1) {
//
//    try {
//
//    }
//
//    }

    return;
}


document.addEventListener('DOMContentLoaded', function() {
    initializeMap();
    dynamicAddWaypointDiv();
    removeWaypointDiv();
});
