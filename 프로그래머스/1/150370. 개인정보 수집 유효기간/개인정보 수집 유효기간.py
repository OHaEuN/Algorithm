def solution(today, terms, privacies):
    answer = []
    
    # terms dict로 저장
    termsDict ={}
    for term in terms:
        name,num = term.split(" ")
        termsDict[name] = int(num)
        
    y,m,d = map(int,today.split("."))
    
    def validatePrivacies (py,pm,pd,term):
        yearDiff = y-py
        monthDiff = m-pm
        dayDiff = d-pd < 0
        diff = yearDiff*12 + monthDiff
        if not dayDiff:
            diff +=1
        if diff > termsDict[term]:
            return True
        else:
            return False
    
    # privacies 순회하면서 privacy 년월일,term 입력받아 계산하는 함수 실행
    # true 반환했을 때 인덱스를 answer에 저장
    for index,privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        py,pm,pd = map(int,date.split("."))
        if validatePrivacies(py,pm,pd,term):
            answer.append(index+1)
    return answer


# 일부터 비교
# today가 기준일보다 작으면 25.05.03 - 24.06.02

# 경과일 계산
# 12달이 유효기간일 때
# 1 / -1 / 1
# 12*1 + -1 + (음수일 때는 안 지난 것)
# 11달 경과(유효기간보다 하나 작을 때는 지났으면 경과한 것), 안지났으므로
# dayDiff가 음수가 아니면 ???
# 기준일이 지난 것 (+1 하기)
# 기준 달보다 커야 초과한 것으로 계산


