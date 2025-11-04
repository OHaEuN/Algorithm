function solution(clothes) {
    let closet = {};
    clothes.forEach((c)=>{
        const [name,category] = c;
        if (closet[category]) {
            closet[category]++;
        } else {
            closet[category] = 1
        }
    })
    
    const itemCount = Object.values(closet);
    // 해당 종류의 의상을 입지 않는 경우도 고려하여 의상 개수에 1을 더한 값을 누적하여 곱하기
    const answer = itemCount.reduce((a,b) => (a*(b+1)),1)
    // 어떤 의상도 입지 않은 경우 제외
    return answer - 1;
}