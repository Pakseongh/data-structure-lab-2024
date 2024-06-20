# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    result = 0
    stack = []

    for char in input:
        print(char) 
        
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += 1
    
    
    result += len(stack)
    
    return result


result = problem2(input)

assert result == 3
print("정답입니다.")
