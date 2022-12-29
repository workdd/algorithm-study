# algorithm-study
국민대학교 DDPSLab 연구실 내 알고리즘 스터디 진행 12/29 ~

### 스터디 목적
- 대학원생 특성상 알고리즘을 접하기 쉽지않고 연구에만 몰두하는 경향이 있음
- 주기적으로 알고리즘을 접하는 기회로써 스터디를 이용

### 스터디 방식
- 매주 하루 (목요일) 주간 풀어온 문제들에 대한 풀이, 논리 공유
- 스터디원의 각 풀이에 대한 시간복잡도, 공간복잡도를 계산해보며 효율성 탐구
- 인원별 풀이 코드 폴더 생성, 본 레포지토리를 Fork 한 후 PR로 합치는 방식으로 코드 정리

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
