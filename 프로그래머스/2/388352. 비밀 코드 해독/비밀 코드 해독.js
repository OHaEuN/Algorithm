function combinations(n){
    let result = []
    
    function addCombination(num, cnt, arr){
        if (cnt === 5){
            result.push([...arr]);
            return;
        }
        
        for (let i = num+1; i<=n; ++i){
            arr.push(i);
            addCombination(i,cnt+1,arr);
            arr.pop();
        }
    }
    
    addCombination(0,0,[]);
    
    return result
}


function solution(n, q, ans) {
    let combi = combinations(n);
    
    for (let i = 0; i < q.length; ++i){
        const set = new Set(q[i]);
        
        combi = combi.filter((com)=>{
            let match = 0;
            com.forEach((c)=>{
                if (set.has(c)) match++; 
            })
            return match === ans[i];
        })
    }
    
    
    return combi.length;
}