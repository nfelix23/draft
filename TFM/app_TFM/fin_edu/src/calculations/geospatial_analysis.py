import folium
import geopandas as gpd
import urbanpy as up

def plot_geospatial_data(school_locations, data, feature):
    m = folium.Map(location=[school_locations['latitude'].mean(), school_locations['longitude'].mean()], zoom_start=5)

    for _, row in school_locations.iterrows():
        school_id = row['school']
        feature_value = data[data['school'] == school_id][feature].mean()
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=10,
            popup=f'School: {school_id}, {feature}: {feature_value:.2f}',
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(m)

    return m

def get_and_plot_pois(school_locations):
    pois = up.OsmPois()
    gdf_schools = gpd.GeoDataFrame(
        school_locations,
        geometry=gpd.points_from_xy(school_locations.longitude, school_locations.latitude),
        crs="EPSG:4326"
    )

    m = folium.Map(location=[school_locations['latitude'].mean(), school_locations['longitude'].mean()], zoom_start=5)

    for _, row in gdf_schools.iterrows():
        school_id = row['school']
        pois_around_school = pois.get_pois_around_point((row['latitude'], row['longitude']), radius=1000)
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f'School: {school_id}',
            icon=folium.Icon(color='blue')
        ).add_to(m)

        for _, poi in pois_around_school.iterrows():
            folium.Marker(
                location=[poi.geometry.y, poi.geometry.x],
                popup=f'{poi["name"]}',
                icon=folium.Icon(color='green')
            ).add_to(m)

    return m
