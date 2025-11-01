function solution(maps) {
    const answer = -1;
    const dx = [1,-1,0,0]
    const dy = [0,0,1,-1]
    const n = maps.length
    const m = maps[0].length
    let visited = Array(n).fill().map((_)=>Array(m).fill(false))
    let q = [[0,0,1]]
    visited[0][0] = true
    while(q.length > 0){
        const [x,y,count] = q.shift()
        if (x === m-1 && y === n-1){
            return count
        }
        
        for (let i = 0; i<4; i++){
            const nx = x + dx[i]
            const ny = y + dy[i]
            if (nx>=0 && nx<m && ny>=0 && ny<n){
                if (!visited[ny][nx] && maps[ny][nx] === 1){
                    q.push([nx,ny,count+1])
                    visited[ny][nx] = true
                }
            }
        }
    }
    return answer;
}