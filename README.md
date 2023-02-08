# algorithm-study
국민대학교 DDPSLab 연구실 내 알고리즘 스터디 진행 12/29 ~

### 스터디 목적
- 대학원생 특성상 알고리즘을 접하기 쉽지않고 연구에만 몰두하는 경향이 있음
- 주기적으로 알고리즘을 접하는 기회로써 스터디를 이용
- Python 코드로 알고리즘 구현하는 것에 대한 이해 증진

### 스터디 방식
- 매주 하루 (목요일) 주간 풀어온 문제들에 대한 풀이, 논리 공유
- 스터디원의 각 풀이에 대한 시간복잡도, 공간복잡도를 계산해보며 효율성 탐구
- 인원별 풀이 코드 폴더 생성, 본 레포지토리를 Fork 한 후 PR로 합치는 방식으로 코드 정리
- Python으로 푸는 것을 기본으로 하되 추가적으로 다른 언어로 풀어 업로드하는 것도 가능

### 스터디 문제
- 문제 난이도는 브론즈 1 ~ 골드4 정도로 난이도가 높지 않은 문제 위주로 선택
- 해당 깃허브에서 정리해둔 문제를 주마다 선별, 백준 그룹에 업로드 후 문제 풀기 
  - https://github.com/tony9402/baekjoon

## Python Input 처리
- 한줄, 공백 처리, 데이터의 갯수가 정해져 있을 경우
```
N, M = map(int, input().split())
```

- 1차원 배열로 입력받기
```
arr = list(map(int, input().split()) 
```

- N행으로 이루어진 2차원 배열 입력
```
N = int(input()) # 행렬의 크기

arr = [list(map(int, input().split())) for _ in range(N)]
```

### Input 성능 개선 ( 빠른 입력이 필요할 경우 )
- sys 라이브러리를 활용하여 input() 함수 대신에 아래와 같이 사용
```
import sys
N, M = map(int, sys.stdin.readline().split())
```

## Dequeue 사용법
```
from collections import deque
deq = deque([1,2,3,4])
```
### 사용시 이점
- 배열안 추가와 삭제를 O(1) 시간복잡도로 처리 가능, python의 리스트로 풀 경우 O(N)의 시간복잡도
- rotate 함수로 배열의 순서를 하나씩 좌, 우로 바꿔가야하는 경우 사용시 이점 이경우에도 O(1) 시간복잡도로 처리 가능, 리스트의 경우 O(N)

## deepcopy 사용법
```
import copy
ipt = [1,2,3]
copied_ipt = copy.deepcopy(ipt)
```
### 사용시 이점
- python의 경우 list, dictionary, dequeue등 일반적인 '=' 기호로 복사 시 주소값을 복사하여, 복사한 값을 변경할 경우 원본값이 변경됨 따라서 원본값을 유지하고, 복사본만 변경해야할 때 deepcopy 이용

