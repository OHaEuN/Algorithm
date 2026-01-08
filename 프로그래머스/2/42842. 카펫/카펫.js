function solution(brown, yellow) {
    const size = brown+yellow;
    let answer = [];
    for (i = 3; i <= size/3; i++){
        if (size % i === 0){
            if ((size/i -2)*(i-2) === yellow){
                answer = [i,size/i];
            }
        }
    }
    answer.sort((a,b)=>b-a);
    return answer;
}
