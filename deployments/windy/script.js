const options = {
    key: '4DiD7grFdBErLOqYOnxgE3apSlZTQ3dk', // REPLACE WITH YOUR KEY !!!
    lat: 48,
    lon: -132,
    zoom: 5,
    geojson: "/cproofwebsite/gliderdata/deployments/cproof-deployments.geojson",
    //geojson: "/gliderdata/deployments/cproof-deployments.geojson", 
};


windyInit(options, windyAPI => {
    const { map } = windyAPI;

    const MARKER_ICON_URL = `../assets/images/slocum_glider.png`;

    const slocumIcon = L.icon({
        iconUrl: MARKER_ICON_URL,
        iconSize:     [19, 22],
        iconAnchor:   [9, 11],
        popupAnchor: [0, 0],
    });

    const markers = [];

    var glideLayer = L.layerGroup(null, {name: "Glider Marker"})

    var gliderJSON = $.ajax({
          url:options.geojson,
          dataType: "json",
          success: function(){
            console.log("Gliderdata!!! Yay");
          },
          error: function (xhr) {
            alert(xhr.statusText)
          }
        })
    $.when(gliderJSON).done(function() {
      var glider = gliderJSON.responseJSON
      var gliderLayer = L.geoJson(glider, {
            filter: function(feature, layer) {
              return feature.geometry.coordinates[0] !== 0 && feature.geometry.coordinates[1] !== 0 &&  feature.properties.active == true;
            },
            onEachFeature: function (feature, layer) {
              numPts = feature.geometry.coordinates.length;
              var beg = feature.geometry.coordinates[numPts-1];
              var marker = L.marker([beg[1], beg[0]],
                {icon: slocumIcon}
              );
              glideLayer.addLayer(marker)
            }
      });
      glideLayer.addTo(map);
      gliderLayer.addTo(map);
    });



    // Handle some events. We need to update the rotation of icons ideally each time
    // leaflet re-renders. them.
    //map.on('zoom', updateIconStyle);
    //map.on('zoomend', updateIconStyle);
    //map.on('viewreset', updateIconStyle);
});
