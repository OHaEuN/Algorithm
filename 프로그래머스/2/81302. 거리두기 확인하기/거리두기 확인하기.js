function check_distance(place,x,y,x_len,y_len){
    const dx = [0,0,1,-1]
    const dy = [1,-1,0,0]
    let visited = Array.from(Array(y_len), () => new Array(x_len).fill(0))
    let distance = Array.from(Array(y_len), () => new Array(x_len).fill(0))
    let queue = []
    queue.push([x,y])
    visited[y][x] = 1
    while (queue.length>0){
        let cx, cy;
        [cx, cy] = queue.pop()
        for (let i = 0; i<4; i++){
            const nx =cx+dx[i]
            const ny =cy+dy[i]
            if (0<=nx && nx<x_len && 0<=ny && ny<y_len){
                if (visited[ny][nx]==0 && distance[cy][cx]<2){
                    if (place[ny][nx]=="P"){
                        return true
                    }else if (place[ny][nx]=="O"){
                        queue.push([nx,ny])
                    }
                    visited[ny][nx]=1
                    distance[ny][nx]=distance[cy][cx]+1
                }
            } 
        }
    }
     return false   
    }



function solution(places) {
    let answer = [];
    places.map((place)=>{
        const x_len = place[0].length
        const y_len = place.length
        let ans = 1
        for (let i = 0; i < x_len; i++){
            for (let j = 0; j < y_len; j++){
                if (place[j][i]==="P"){
                    if (check_distance(place,i,j,x_len,y_len)){
                        ans = 0
                    }
                }
            }
        }
        answer.push(ans)
    })
    
    return answer;
}