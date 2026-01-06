function isPalindrome(str) {
    if(str.length <= 1 ) {
        return true
    }
    if (str[0] === str[str.length - 1]) {
        let temp = str.split('')
        temp.pop()
        temp.shift()
        str = temp.join('')
        return isPalindrome(str)
    }
    return false
}

console.log(isPalindrome('212'))