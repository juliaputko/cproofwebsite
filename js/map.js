
// Basemap Layers
var mapboxOSM = L.tileLayer('https://server.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Reference/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri'
});

var mapboxOcean = L.tileLayer('https://server.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri'
});


var featureLayer = L.geoJson(null, {
  style: function (feature) {
    return {
      color: feature.properties.color,
      weight: 4,
      opacity: 0.6,
      fillColor: feature.properties.color,
      fillOpacity: 0.6,
      clickable: true
    };
  },
});

//maybe add before

var argoIcon = L.icon({
  iconUrl: '/cproofwebsite/img/argo-yellow-01.png', ///img/argo-yellow-01.png
  iconSize:     [7, 40],
  iconAnchor:   [18, 22]
});

var glideLayer = L.layerGroup(null, {name: "Glider Marker"})

// This won't actually get added to the map, but will populate glideLayer
var gliderLayer = L.geoJson(null, {
  filter: function(feature, layer) {
    return feature.geometry.coordinates[0] !== 0 && feature.geometry.coordinates[1] !== 0 &&  feature.properties.name == 'argo'; 
  },
  style: function (feature) {
    return {
      color: "#000000",
      weight: 0,
      opacity: 0.0,
      clickable: false
    };
  },
  onEachFeature: function (feature, layer) {
    numPts = feature.geometry.coordinates.length;
    var beg = feature.geometry.coordinates[numPts-1];
    var marker = L.marker([beg[1], beg[0]],
      {icon: argoIcon}
    );
    glideLayer.addLayer(marker)
  }
});


//jpend 




/////slocum icon 
var slocumIcon = L.icon({
  iconUrl: '/cproofwebsite/gliderdata/deployments/assets/images/slocum_glider.png',
  iconSize:     [38, 45],
  iconAnchor:   [18, 22]
});

var glideLayer2 = L.layerGroup(null, {name: "Glider Marker"})

// This won't actually get added to the map, but will populate glideLayer
var gliderLayer2 = L.geoJson(null, {
  filter: function(feature, layer) {
    return feature.geometry.coordinates[0] !== 0 && feature.geometry.coordinates[1] !== 0 &&  feature.properties.active == false; //&&  feature.properties.active == false; //jp changed to false
  },
  style: function (feature) {
    return {
      color: "#000000",
      weight: 0,
      opacity: 0.0,
      clickable: false
    };
  },
  onEachFeature: function (feature, layer) {
    numPts = feature.geometry.coordinates.length;
    var beg = feature.geometry.coordinates[numPts-1];
    var marker = L.marker([beg[1], beg[0]],
      {icon: slocumIcon}
    );
    glideLayer2.addLayer(marker)
  }
});


//jpend 

// Fetch the GeoJSON file
$.getJSON("cproofwebsite/gliderdata/deployments/cproof-deployments_all.geojson", function (data) {
  geojson = data;
  features = $.map(geojson.features, function(feature) {
    return feature.properties;
  });
  featureLayer.addData(data);
  gliderLayer.addData(data); //jp add 
  gliderLayer2.addData(data); //jp add 
  $("#loading-mask").hide();
});

var map = L.map("mapfront", {
  layers:  [mapboxOcean, mapboxOSM, featureLayer, glideLayer,gliderLayer2] //jpnote added glideLayer
}).setView([50., -133], zoom=5)


// Larger screens get expanded layer control
if (document.body.clientWidth <= 767) {
  isCollapsed = true;
} else {
  isCollapsed = false;
}
var baseLayers = {
  "Ocean Labels": mapboxOSM,
};

var layerControl = L.control.layers(baseLayers, overlayLayers, {
}).addTo(map);
