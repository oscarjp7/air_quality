import geopandas as gpd
import pandas as pd
from DATA.prepdata import get_gdf_data
from DATA.visdata import plot_pollutant_borough, plot_pollutant_data

# Choose pollutant to map
valid_pollutant = ['NO2', 'NOx', 'PM10', 'PM10d', 'PM25']
pollutant=''
while pollutant not in valid_pollutant:
    print('Choose pollutant: NO2, NOx, PM10, PM10d, PM25')
    pollutant=input('-> ')

# Choose plots
conc_per_borough = ''
while conc_per_borough != 'n' and conc_per_borough != 'y':
    print('Plot the mean pollution per Borough? [y/n]')
    conc_per_borough = input('-> ')
conc_distribution = ''
while conc_distribution != 'n' and conc_distribution != 'y':
    print('Plot the pollution concentration? [y/n]')
    conc_distribution = input('-> ')

# Load pollutant data from 2013, 2016 and 2019
print('Loading data')
data_2019 = pd.read_csv(f'raw_data/Concentration_data/2019/laei_LAEI2019v3_CorNOx15_{pollutant}.csv')
data_2016 = pd.read_csv(f'raw_data/Concentration_data/2016/LAEI2016_2016_{pollutant}.csv')
data_2013 = pd.read_csv(f'raw_data/Concentration_data/2013/PostLAEI2013_2013_{pollutant}.csv')

# Load London Borough data
boroughs = gpd.read_file('raw_data/statistical-gis-boundaries-london/ESRI/London_Ward_CityMerged.shp')
print('Done')

# Turn pollutant data into gdf data
print('Transforming to GDF')
sample_size = 50000
gdf_data_2019 = get_gdf_data(boroughs, data_2019, sample_size, 2019)
gdf_data_2016 = get_gdf_data(boroughs, data_2016, sample_size, 2016)
gdf_data_2013 = get_gdf_data(boroughs, data_2013, sample_size, 2013)
print('Done')

# Join borough and pollutant data
print('Merging data')
joined_pollutant_data = pd.concat([gdf_data_2019,gdf_data_2016,gdf_data_2013])
joined_data = gpd.sjoin(boroughs, joined_pollutant_data, how='left')
print('Done')

# Plot pollutant concentration per borough
if conc_per_borough == 'y':
    print(f'Creating {pollutant} per borough concentration map')
    plot_pollutant_borough(joined_data, boroughs, pollutant)
    print('Done')

if conc_distribution == 'y':
    print(f'Creating {pollutant} concentration map')
    plot_pollutant_data(joined_pollutant_data, pollutant)
    print('Done')
