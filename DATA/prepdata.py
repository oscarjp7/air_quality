import geopandas as gpd
from shapely.geometry import Point

def get_gdf_data(boroughs, data, size, year):
    data = data.sample(n=size, random_state=42)

    geometry = [Point(xy) for xy in zip(data['x'], data['y'])]
    data_gdf = gpd.GeoDataFrame(data, geometry=geometry)

    data_gdf.crs = boroughs.crs

    if 'conct' in data_gdf.columns:
        data_gdf.rename(columns={'conct':'conc'}, inplace=True)

    data_gdf=data_gdf[['conc','geometry']]

    new_conc=f'{year}_data'
    data_gdf.rename(columns={'conc':new_conc}, inplace=True)
    return data_gdf
