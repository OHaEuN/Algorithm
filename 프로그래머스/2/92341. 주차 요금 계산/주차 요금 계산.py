import math
def solution(fees, records):
    answer = []
    cars = dict()
    cars_time = dict()
    
    # 전체 시간 계산
    def calculateTime(i_time,o_time):
        i_hour,i_min = map(int,i_time.split(":"))
        o_hour,o_min = map(int,o_time.split(":"))
        total_time = 0
        if i_min<=o_min:
            total_time = 60*(o_hour-i_hour) + (o_min - i_min)
        else:
            total_time = 60*(o_hour-i_hour-1) + 60-(i_min - o_min)
        return total_time
    
    # 시간에 따른 요금 계산
    def calculateFee(total_time):
        fee = fees[1]
        if total_time > fees[0]:
            fee += math.ceil((total_time-fees[0])/fees[2])*fees[3]
        return fee
    
    # 출차/입차 처리
    for record in records:
        time,car,in_out = record.split(' ')
        if in_out == "IN":
            cars[car]=time
            if car not in cars_time:
                cars_time[car]=0
                
        if in_out == "OUT":
            if car in cars:
                cars_time[car]+=calculateTime(cars[car],time)
                cars[car] = "0"
                
    # OUT 없이 남아있는 차량
    for c in cars:
        if cars[c]!="0":
            cars_time[c]+=calculateTime(cars[c],"23:59")
    
    sorted_cars = sorted(cars_time.items())
    for car in sorted_cars:
        answer.append(calculateFee(car[1]))
    
    return answer