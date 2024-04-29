function initializeMap() {
    var map = L.map('leaflet-map').setView([43.65, -79.35], 10);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
}


document.addEventListener('DOMContentLoaded', function() {
    initializeMap();
});
