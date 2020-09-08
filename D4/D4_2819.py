import sys

sys.stdin = open("D4_2819_input.txt", "r")

def grid_sum():
    for x in range(4):
        for y in range(4):
            # 16개 점을 각각 출발점으로 움직이며 문자열을 생성
            move(x,y, str(grid[x][y]))
    

# 재귀를 이용하여 가능한 모든 점에 대해 계산
# 16개 출발점에 대해 4^7*16 ~ 2^18이므로 시간제한을 넘지 않음
def move(x, y, temp):
    # 문자열의 길이가 7이되면 stop하고 문자열을 넘겨줌
    if len(temp) == 7:
        result.add(temp)
        return
    # 위처럼 set을 쓰는 방법 말고 visit=[0]*10000000 만들어서
    # visit[temp]에 하나씩 기록해주는 방법도 존재
    # 단 리스트가 너무 길어 매 testcase마다 생성하면 overflow
    # 한번만 만들고 visit[temp] = tc식으로 해줘야 함
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]        
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            # str concatenation을 이용하여 문자열에 숫자를 추가
            move(nx, ny, temp+str(grid[nx][ny]))
            # # 아래와 같이 자릿수를 하나씩 밀어주는 게 더 빠르다
            # move(nx, ny, temp*10+(grid[nx][ny]))


t = int(input())
for test_case in range(t):    
    grid = [list(map(int, input().split())) for _ in range(4)]   
    # 집합 자료형을 이용하여 중복 제거
    result = set()    
    grid_sum()
    # 집합의 원소 수만을 출력하면 OK
    print('#' + str(test_case + 1), len(result))
