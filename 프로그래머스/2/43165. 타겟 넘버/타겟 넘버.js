function solution(numbers, target) {
    let answer = 0;
    const len = numbers.length;
    
    function dfs(s, i) {
        if (i === len) {
            if (s === target) {
                answer++;
            }
            return;
        }
        
        dfs(s + numbers[i], i + 1); 
        dfs(s - numbers[i], i + 1);
    }
    
    dfs(0, 0);
    return answer;
}