function getItemsAt(arr, pos) {
    let flag = false;

    return (function getItemsAtHelper(arr, pos) {
        if (pos == "even" && arr.length == 2) {
            arr.splice(1)
            return arr
        } else if (pos == "odd" && arr.length == 1) {
            return arr
        } else {
            result = getItemsAtHelper(arr.splice(1), pos)
            if (flag) {
                flag = false
                return arr.concat(result)
            } else {
                flag = true
                return result
            }
        }
    })(arr, pos)
}

console.log(getItemsAt(["stuff", "in", "here", "is", "great"], "even"))
console.log(getItemsAt(["stuff", "in", "here", "is", "great"], "odd"))