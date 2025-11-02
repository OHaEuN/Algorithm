function solution(word) {
    const words = ['A','E','I','O','U']
    let dict = [...words]
    for (let i = 1; i<5; i++){
        for (const d of dict){
            if (d.length === i){
                for (const w of words){
                    dict.push(d+w)
                }
            }
        }
    }
    dict.sort();
    return dict.indexOf(word)+1;
}