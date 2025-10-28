import pandas as pd

# -----------------------------
# CSV 파일 읽기
# -----------------------------
# header=None : 제목(열 이름)이 없을 때
# header=0    : 첫 번째 줄을 열 이름으로 사용할 때 (기본값)
# header=1    : 두 번째 줄을 열 이름으로 사용할 때
# index_col=0 : 첫 번째 열을 인덱스로 사용
df = pd.read_csv('read.csv', encoding='utf-8', index_col=0, header=0)
print("[원본 데이터]")
print(df)
print()

# 결측값 조회
print("[결측값 조회]")
print(df.isna())       # 결측값이면 True
print()

# 결측값이 아닌 값 조회
print("[결측값이 아닌 값 조회]")
print(df.notna())      # 결측값이 아니면 True
print()

# 결측값 제거
print("[결측값이 포함된 행 제거]")
print(df.dropna())     # 결측값이 있는 행 전체 제거
print()

print("[특정 열 기준 결측값 제거: subset=['kor', 'eng']]")
print(df.dropna(subset=['kor', 'eng']))  # 특정 열만 기준으로 제거
print()

# 결측값 대체
print("[결측값 대체]")
df = df.fillna({'kor': 22, 'eng': 30})   # 결측값을 지정값으로 채우기
print(df)
