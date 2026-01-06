function solution(progresses, speeds) {
    let answer = [];
    const days = progresses.map((p,i)=>{
        const remain = 100 - p
        const speed = speeds[i];
        if (remain % speed !== 0){
            return Math.floor(remain/speed)+1; 
        }
        return Math.floor(remain/speed);
    })
    const len = days.length;
    let stack = [];
    for (let i = 0; i < len; i++){
        if (stack.length > 0){
            if (stack[0] >= days[i]){
                stack.push(days[i]);
            } else {
                answer.push(stack.length);
                stack = [days[i]];
            }
        } else {
            stack.push(days[i]);
        }
    }
    if (stack.length > 0){
        answer.push(stack.length);
    }
    return answer;
}