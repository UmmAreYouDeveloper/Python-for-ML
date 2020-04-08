import pandas as pd
from io import StringIO

csv_data = '''A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,,7.0
10.0,11.0,12.0'''

df = pd.read_csv(StringIO(csv_data))
df.dropna(axis=1)
print(df)
df.dropna(how="all")
print(df)
df.dropna(subset=['C'])
print(df)
df.dropna(thresh=4)
print(df)
df.fillna(df.mean())
"""
    file을 흉내내는 StringIO
    파일처럼 취급되는 객체를 만들어낸다. 단, 실제 파일객체는 아니다.
    파일 객체에 쓰이는 함수들이 그대로 적용
    f = StringIO() : 객체를 생성하는 함수
    f.read()
    자주쓰이는 이유 : 가끔 문자열 데이터를 파일에 저장한 다음에 여러가지 처리를 하는데,
    하지만 그 파일이 다시쓰이지 않고, 꼭 저장될 필요가 없다면 파일을 저장할 필요가 없을 것
    이렇게 꼭 파일을 만들어서 처리를 할 필요가 없게 해주는 모듈이 바로 StringIO

"""
