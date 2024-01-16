def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = []  # 다리 위 남은 거리
    bridge_weights = []  # 다리 위 트럭의 무게

    while bridge or truck_weights:
        count += 1

        if bridge:
            bridge = [(truck, time - 1) for truck, time in bridge]  # 1만큼 전진
            if bridge[0][1] == 0:  # 도착한 트럭 제거
                bridge_weights.pop(0)
                bridge.pop(0)

        if truck_weights and sum(bridge_weights) + truck_weights[0] <= weight:
            bridge.append((truck_weights[0], bridge_length))
            bridge_weights.append(truck_weights.pop(0))

    return count
