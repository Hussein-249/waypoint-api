var additionalWaypoints = 1

function initializeMap() {
    // setting the map in the 'leaflet-map' div
    var map = L.map('leaflet-map').setView([43.65, -79.35], 8);

    // tile layer must be specified, else blank map
    L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.opentopomap.org/copyright">OpenTopoMap</a>'
    }).addTo(map);
}


function dynamicAddWaypointDiv() {
    var addWayPointButton = document.getElementById('add-button');
    var form = document.querySelector('form');

    addWayPointButton.addEventListener('click', function() {

        additionalWaypoints++;

        var waypointInput = document.createElement('input');
        waypointInput.setAttribute('type', 'text');
        waypointInput.setAttribute('id', 'waypoint-' + additionalWaypoints);
        waypointInput.setAttribute('name', 'waypoint-' + additionalWaypoints);

        var waypointLabel = document.createElement('label');
        waypointLabel.setAttribute('for', 'waypoint-' + additionalWaypoints);
        waypointLabel.textContent = 'Point ' + additionalWaypoints;

        form.appendChild(document.createElement('br'));
        form.appendChild(waypointLabel);
        form.appendChild(document.createElement('br'));
        form.appendChild(waypointInput);
        form.appendChild(document.createElement('br'));
    });
}


document.addEventListener('DOMContentLoaded', function() {
    initializeMap();
    dynamicAddWaypointDiv();
});
