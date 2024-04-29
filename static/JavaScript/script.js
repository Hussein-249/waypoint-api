// importing jQuery
import $ from "https://code.jquery.com/jquery-3.6.0.min.js";


$(document).ready( () => {
    $('#submit-button').click( (e) => {
    e.preventDefault();
    var origin = $('#origin').val();
    var destination = $('#dest').val();

     $.ajax({
            url: '/submit_form',
            type: 'GET',
            data: {
                origin: origin,
                origin: destination
            },
            success: function(response) {
                updateMap(response);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
    });
});

function updateMap()
{
    var map = L.map('leaflet-map').setView([51.505, -0.09], 13);

    map.eachLayer(function (layer) {
            if (layer instanceof L.Marker) {
                map.removeLayer(layer);
            }
        });

    var marker = L.marker([response.lat, response.lon]).addTo(map);

    map.fitBounds(marker.getBounds());

}
