import folium
from folium.plugins import MarkerCluster
import pandas as pd

df = pd.read_csv('file/starbucksFile.csv')

# location 중심 위치 화면에 표시
starbucks = folium.Map(location=[37.566730, 126.978290], zoom_start=30)

print(df)

for i in range(len(df)):
    folium.Marker(
        location=[df.loc[i, "위도"].astype(float), df.loc[i, "경도"].astype(float)],
        popup=df.loc[i, "지점명"],
        icon=folium.Icon(color='green', icon='coffee', prefix='fa')
    ).add_to(starbucks)

starbucks.save('starbucksMarker.html')


