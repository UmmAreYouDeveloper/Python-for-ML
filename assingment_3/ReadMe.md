# Assignment_3

## 유용했던 link 모음
  [](https://www.kdata.or.kr/info/info_04_view.htmlfield=&keyword=&type=techreport&page=25&dbnum=181570&mode=detail&type=techreport)

## Data split
+ 총 주어진 샘플 중 80%를 training으로 구성하여 훈련
+ 10%를 validation 데이터로 구성하여 하이퍼 파라미터를 최적화 시킨다.
+ 최종적으로 남은 10%를 test 데이터로 구성한다.
``` python
  from sklearn.model_selection import train_test_split
  train_test_split(arrays, test_size, train_size, random_state, shuffle, stratify)
```
+ (1) Parameter
  - arrays : 분할시킬 데이터를 입력 (Python list, Numpy array, Pandas dataframe 등..)
  - test_size : 테스트 데이터셋의 비율(float)이나 갯수(int) (default = 0.25)
  - train_size : 학습 데이터셋의 비율(float)이나 갯수(int) (default = test_size의 나머지)
  - random_state : 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값 (int나 RandomState로 입력)
  - shuffle : 셔플여부설정 (default = True)
  - stratify : 지정한 Data의 비율을 유지한다. 예를 들어, Label Set인 Y가 25%의 0과 75%의 1로 이루어진 Binary Set일 때, stratify=Y로 설정하면                  나누어진 데이터셋들도 0과 1을 각각 25%, 75%로 유지한 채 분할된다.
+ (2) Return
  - X_train, X_test, Y_train, Y_test : arrays에 데이터와 레이블을 둘 다 넣었을 경우의 반환이며, 데이터와 레이블의 순서쌍은 유지된다.
  - X_train, X_test : arrays에 레이블 없이 데이터만 넣었을 경우의 반환
+ (3) Example
``` python
import numpy as np
from sklearn.model_selection import train_test_split

X = [[0,1],[2,3],[4,5],[6,7],[8,9]]
Y = [0,1,2,3,4]

# 데이터(X)만 넣었을 경우
X_train, X_test = train_test_split(X, test_size=0.2, random_state=123)
# X_train : [[0,1],[6,7],[8,9],[2,3]]
# X_test : [[4,5]]

# 데이터(X)와 레이블(Y)을 넣었을 경우
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=321)
# X_train : [[4,5],[0,1],[6,7]]
# Y_train : [2,0,3]
# X_test : [[2,3],[8,9]]
# Y_test : [1,4]
```

※ 사용방법이 쉽고 셔플까지 적용되므로 간단하고 합리적인 함수이지만 Validation Set을 따로 만들어주지는 않는다. 
   Validation Set이 필요하다면 분할한 데이터 중 한 덩어리에 해당 함수를 한 번 더 사용하면 된다.
   
## Using Algorithm package in sklearn

+ [sklearn tutorial](https://scikit-learn.org/stable/)
+ Google Search Keywords
  - sklearn <algorithm name>

## Using cross-validation(k-fold, loocv) package in sklearn
+ Google Search Keywords
  - sklearn <cv name>
  
## GridSearchCV and make_pipeline
+ Google Search Keywords
  - sklearn GridSearchCV
  - sklearn pipeline
