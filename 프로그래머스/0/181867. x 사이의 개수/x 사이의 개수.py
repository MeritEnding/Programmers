def solution(myString):
    answer = []
    answer=myString.split('x')
    
    result=[]
    for i in answer:
        result.append(len(i))
    
    return result