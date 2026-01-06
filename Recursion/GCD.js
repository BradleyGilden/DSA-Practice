function gcd(num1, num2) {
    let a, b
    if (num1 > num2) {
        a = num1, b = num2
    } else {
        a = num2, b = num1
    }
    function calculate(a, b) {
        if (b === 0) {
            return a
        }
        return calculate(b, a % b)
    }

    console.log(calculate(a, b))
}

gcd(9, 6)