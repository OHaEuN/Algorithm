function solution(players, m, k) {
    let answer = 0;
    const count = new Array(24).fill(0);
    players.forEach((p, time)=>{
        const new_server = Math.floor(p / m) - count[time];
        
        if (new_server > 0) {
            answer += new_server;
            for (let i = 0; i < k; i++) {
                count[time+i] += new_server;
            }
        }
    })
    
    return answer;
}