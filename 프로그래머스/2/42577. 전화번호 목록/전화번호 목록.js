function solution(phone_book) {
    const len = phone_book.length;
    const sorted_book = phone_book.slice().sort();
    for (let i = 0; i < len-1; i++){
        if (sorted_book[i+1].startsWith(sorted_book[i])){
            return false;
        }
    }
    return true;
}