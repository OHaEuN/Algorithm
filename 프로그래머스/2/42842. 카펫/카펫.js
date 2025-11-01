function solution(brown, yellow) {
    const sum = brown + yellow;
    
    for (let height = 3; height <= brown; height++){
        if (sum % height === 0){
            const width = sum / height
            
            if ((width-2)*(height-2) === yellow){
                return [width,height]
            }
        }
    }
}