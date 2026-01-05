
function flatten(arr) {
    const temp = []
    function flat(arr) {
        for (let i of arr) {
            if (!Array.isArray(i)) {
                temp.push(i)
            }
            else flat(i)
        }
    }
    flat(arr)
    return temp
}


console.log(flatten([1, [2, [3, 4], 5]]))