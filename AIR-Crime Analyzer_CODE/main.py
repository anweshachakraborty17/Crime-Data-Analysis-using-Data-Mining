# for some basic operations
import numpy as np 
import pandas as pd 

# for visualizations
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import squarify

data = pd.read_csv('crime.csv')
# check the shape of the data
print(data.shape)

#To see the first 5 rows in the data set
print(data.head())

#To Describe the data set
print(data.describe())

#To check if there are any null values
print(data.isnull().sum())

#Filling the missing value in PdDistrict using the mode values
data['PdDistrict'].fillna(data['PdDistrict'].mode()[0], inplace = True)
print(data.isnull().any().any())

###### Data Visualization ######

#Different categories of crime___Figure 1 

plt.rcParams['figure.figsize'] = (10, 10)
#plt.style.use('seaborn')
plt.style.use('dark_background')
sns.countplot(data['Category'], palette = 'gnuplot')

plt.title('Major Crimes in West Bengal', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90)

#plt.show()


#Plotting a tree map___Figure 2

#plt.style.use('seaborn')
plt.style.use('dark_background')
y = data['Category'].value_counts().head(15)

plt.rcParams['figure.figsize'] = (10, 10)
plot2 = plt.figure(2) #plotfigure2

#plt.style.use('fivethirtyeight')
color = plt.cm.magma(np.linspace(0, 1, 15))
squarify.plot(sizes = y.values, label = y.index, alpha=.9, color = color)

plt.title('Tree Map for Top 15 Crimes in West Bengal', fontweight = 30, fontsize = 20)
plt.axis('off')
plot3 = plt.figure(3) #plotfigure3
#plt.show()


#Description of the Crime___Figure 3
from wordcloud import WordCloud

#plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (10, 10)

plt.style.use('fast')
wc = WordCloud(background_color = 'orange', width = 1500, height = 1500).generate(str(data['Descript']))

plt.title('Description of the Crime', fontweight = 30, fontsize = 20)
plt.imshow(wc)

plt.axis('off')
plot4 = plt.figure(4) #plotfigure4
#plt.show()


#Regions with count of crimes___Figure 4
plt.rcParams['figure.figsize'] = (10, 10)
#plt.style.use('seaborn')

#plt.style.use('dark_background')
#plt.style.use('fivethirtyeight')

color = plt.cm.spring(np.linspace(0, 1, 15))
data['PdDistrict'].value_counts().plot.bar(color = color, figsize = (10, 10))

plt.title('District with Most Crime',fontsize = 20)
plt.xticks(rotation = 90)

plot5 = plt.figure(5) #plotfigure5
#plt.show()


#Top 15 Addresses in Kolkata in Crime___Figure 5
#plt.style.use('seaborn')

plt.rcParams['figure.figsize'] = (10, 10)
color = plt.cm.ocean(np.linspace(0, 1, 15))

data['Address'].value_counts().head(15).plot.bar(color = color, figsize = (10, 10))
plt.title('Top 15 Regions in Crime',fontsize = 20)

plt.xticks(rotation = 90)
plot6 = plt.figure(6) #plotfigure6

#plt.show()


#Crimes in Each Month___Figure 6
data['Date'] = pd.to_datetime(data['Date'])

data['Month'] = data['Date'].dt.month

#plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (10, 10)

sns.countplot(data['Month'], palette = 'winter',)
plt.title('Crimes in each Months', fontsize = 20)

plot7 = plt.figure(7) #plotfigure7
#plt.show()


#Regions with Days of crimes___Figure 7
#plt.style.use('seaborn')
data['DayOfWeek'].value_counts().head(15).plot.pie(figsize = (10, 10), explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01))

plt.title('Crime count on each day',fontsize = 20)
plt.xticks(rotation = 90)

plot8 = plt.figure(8) #plotfigure8
#plt.show()


#Checking the time at which crime occurs mostly___Figure 8
import warnings
warnings.filterwarnings('ignore')

color = plt.cm.twilight(np.linspace(0, 5, 100))
data['Time'].value_counts().head(20).plot.bar(color = color, figsize = (10, 10))

plt.title('Distribution of crime over the day', fontsize = 20)
#plt.show()


#District vs Category of Crime___Figure 9
#plt.style.use('seaborn')
df = pd.crosstab(data['Category'], data['PdDistrict'])
color = plt.cm.Greys(np.linspace(0, 1, 10))

df.div(df.sum(1).astype(float), axis = 0).plot.bar(stacked = True, color = color, figsize = (10, 10))
plt.title('Crime location vs Category of Crime', fontweight = 30, fontsize = 20)

plt.xticks(rotation = 90)
plot9 = plt.figure(9) #plotfigure9
#plt.show()

###### DISPLAY ######

plt.show()


###### Geographical Visualization ######
t = data.PdDistrict.value_counts()

table = pd.DataFrame(data=t.values, index=t.index, columns=['Count'])
table = table.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])

table = table.reset_index()
table.rename({'index': 'Neighborhood'}, axis='columns', inplace=True)

print(table)


#gjson = r'https://cocl.us/sanfran_geojson'
#sf_map = folium.Map(location = [37.77, -122.42], zoom_start = 12)


##Density of crime in Kolkata
##generate map
#sf_map.choropleth(
    #geo_data=gjson,
    #data=table,
    #columns=['Neighborhood', 'Count'],
    #key_on='feature.properties.DISTRICT',
    #fill_color='YlOrRd', 
    #fill_opacity=0.7, 
    #line_opacity=0.2,
    #legend_name='Crime Rate in Kolkata'
#)

#sf_map


