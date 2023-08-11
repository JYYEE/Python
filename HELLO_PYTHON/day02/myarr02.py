# 배열 추가 append - 배열 안에 추가
# 배열 추가 insert(0, data) - 배열 인덱스 0의 자리에 data를 추가하고 나머지 데이터는 뒤로 밀림.


arr = ["홍길동", "전우치", "이순신"];
arr.append("유관순")
arr.insert(0, "윤봉길")
arr.insert(len(arr), "안중근") # 맨마지막에 추가하는 것과 같음. 즉, append와 같은 표현.

print(arr)