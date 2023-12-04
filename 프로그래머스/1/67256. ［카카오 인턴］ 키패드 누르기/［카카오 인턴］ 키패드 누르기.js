function solution(numbers, hand) {
    let answer = '';
    const keyboard = [[1,4,7],[2,5,8,0],[3,6,9]]
    let current_L=[0,3]; // 최근 누른 번호의 좌표 저장
    let current_R=[2,3]; 
    numbers.map((n)=>{
        if (keyboard[0].includes(n)){
            answer +="L"
            current_L =[0,keyboard[0].indexOf(n)]
        }else if (keyboard[1].includes(n)){ // 가운데일때
            const x = 1
            const y = keyboard[1].indexOf(n)
            if (Math.abs(current_L[0]-x)+Math.abs(current_L[1]-y)<Math.abs(current_R[0]-x)+Math.abs(current_R[1]-y)){
                answer +="L"
                current_L = [x,y]
            }else if (Math.abs(current_L[0]-x)+Math.abs(current_L[1]-y)>Math.abs(current_R[0]-x)+Math.abs(current_R[1]-y)){
                answer +="R"
                current_R = [x,y]
            }else{
                if(hand==="right"){
                answer +="R"
                current_R = [x,y]
                }else{
                answer +="L"
                current_L = [x,y]
                }
            }
        }else{
            answer +="R"
            current_R =[2,keyboard[2].indexOf(n)]
        }
    })
    return answer;
}