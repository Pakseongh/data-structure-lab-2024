# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = 0
    median = 0
    result = [0,0]
    
    mean = sum(input) / len(input)
    sorted_input = sorted(input)
    n = len(sorted_input)
    if n % 2 == 1:
        median = sorted_input[n // 2]
    else:
        median = (sorted_input[n // 2 - 1] + sorted_input[n // 2]) / 2
    
    result[0] = mean
    result[1] = median
    
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")