function solution(s) {
    let answer = [];
    const s_arr = Array.from(s)
    const word = ["zero","one","two","three","four","five","six","seven","eight","nine"] 
    let stack = []
    s_arr.map((s)=>{if (isNaN(s)){
                    stack.push(s)
                }else {
                    answer.push(s)
                }
                const current = stack.join('')
                
                if (word.includes(current)){
                    answer.push(String(word.indexOf(current)))
                    stack = []
                }
               })
    return Number(answer.join(""));
}