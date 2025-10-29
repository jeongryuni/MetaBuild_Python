import folium
print(folium.__version__)

# location 중심 위치 화면에 표시
m = folium.Map(location=[37.658978, 127.181755], zoom_start=30)
m.save('map1.html')

# 위치에 빨간 마커 표시하기
folium.Marker(location=[37.658978, 127.181755], popup='집', icon=folium.Icon(color='red')).add_to(m)
m.save('map2.html')

# 마커에 아이콘(모양) 넣기
folium.Marker(location=[37.241502867572024, 131.86754915841234],
              popup="독도",
              icon=folium.Icon(color='green', icon="star")).add_to(m)
m.save("map3.html")

# 원형 마커 (CircleMarker) 추가
folium.CircleMarker(
    location=[78.92344067552835, 11.93202143993465],
    popup="북극다산과학기지",
    color='red',
    fill_color='red',
    zoom_start=30
).add_to(m)
m.save("map4.html")  # 원형 마커가 추가된 지도 저장 (map4.html)

# 새로운 지도 생성 (이전 마커들 초기화됨)
m = folium.Map(location=[37.487841, 127.039141],zoom_start=10)
m.save("map5.html")

# 로또 위치 찍기
lotto = [
  {"store":"담배","loc":[37.62585944357624,127.01847823823798]},
  {"store":"화곡본마트","loc":[37.54248103738589,126.84414659211494]},
  {"store":"용꿈돼지꿈","loc":[37.5447438346992,126.95223862043447]},
  {"store":"일이오마켓","loc":[37.47943673430032,126.98346178441342]},
  {"store":"여명슈퍼마켓","loc":[37.61432815661055,127.0415039221072]},
  {"store":"5가로또레드탑","loc":[37.570756251987575,127.00235901546226]},
  {"store":"복권세상","loc":[35.91885025656432,128.55034430109828]},
  {"store":"복권전문점","loc":[37.50384327747725,126.71513104367074]},
  {"store":"인현동지하가판","loc":[37.47627910055104,126.63147671205866]},
  {"store":"CU(광주서동점)","loc":[35.14814807640179,126.90555219336346]},
  {"store":"지산로또방","loc":[35.148338888178,126.93203920504686]},
  {"store":"천사로또방","loc":[37.63618838692431,127.21107884503209]},
  {"store":"오렌지통신","loc":[37.42889361993242,127.10232604117991]},
  {"store":"여수복권방","loc":[37.418353650942116,127.12640523182601]},
  {"store":"둘리복권방","loc":[37.34532813934063,126.73627994929885]},
  {"store":"금성24시편의점","loc":[37.84401249737699,127.06236893072152]},
  {"store":"GS25(청주주은점)","loc":[36.60987111587086,127.49134026856717]},
  {"store":"장미슈퍼","loc":[36.276304155315685,126.90940713047799]},
  {"store":"장미슈퍼","loc":[36.276304155315685,126.90940713047799]},
  {"store":"아이24(수송점)","loc":[35.970108052787594,126.7189421934312]},
  {"store":"탑로또","loc":[34.87844231008963,128.62803523643754]}
]


# MarkerCluster 가까운 위치는 숫자로 표시
from folium.plugins import MarkerCluster
maker_cluster = MarkerCluster().add_to(m)

for i in range(len(lotto)):
    folium.Marker(location=lotto[i]["loc"],
                  popup=lotto[i]["store"],
                  icon=folium.Icon(color='red', icon='star')).add_to(maker_cluster)

m.save("map6.html")