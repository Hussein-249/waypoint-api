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

    addWayPointButton.addEventListener('click', function() {

        if (additionalWaypoints >= 4) {
            pass;
        } else {

            if (additionalWaypoints == 3)
            {
                addWayPointButton.innerHTML = 'Max Pts';
            }

            additionalWaypoints++;

            var waypointDiv = document.createElement('div');
            waypointDiv.setAttribute('id', 'waypoint-div-' + additionalWaypoints);

            var waypointInput = document.createElement('input');
            waypointInput.setAttribute('type', 'text');
            waypointInput.setAttribute('id', 'waypoint-nr-' + additionalWaypoints);
            waypointInput.setAttribute('name', 'waypoint-nr-' + additionalWaypoints);
            waypointInput.setAttribute('class', 'text-black text-sm px-2 mb-4 bg-gray-200 rounded');

            var waypointLabel = document.createElement('label');
            waypointLabel.setAttribute('for', 'waypoint-nr-' + additionalWaypoints);
            waypointLabel.setAttribute('id', 'waypoint-label-' + additionalWaypoints);
            waypointLabel.textContent = 'Point ' + additionalWaypoints;

            waypointDiv.appendChild(waypointLabel);
            waypointDiv.appendChild(document.createElement('br'));

            waypointDiv.appendChild(waypointInput);
            waypointDiv.appendChild(document.createElement('br'));

            form.appendChild(waypointDiv);
        }
    });
}


function removeWaypointDiv() {
    var addWayPointButton = document.getElementById('add-button');
    var removeWayPointButton = document.getElementById('remove-button');
    var form = document.getElementById('add-waypoint-section');

    removeWayPointButton.addEventListener('click', function() {

        try {
            var targetDiv = document.getElementById('waypoint-div-' + additionalWaypoints);
            if (additionalWaypoints > 1) {
                form.removeChild(targetDiv);
                additionalWaypoints--;
                addWayPointButton.innerHTML = '+ Waypt';

            }
        } catch (err) {
            console.log('RemoveButtonError: ', err);
        }
    });
}


 const ctx = document.getElementById('elevation-chart');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

document.addEventListener('DOMContentLoaded', function() {
    initializeMap();
    dynamicAddWaypointDiv();
    removeWaypointDiv();
});
