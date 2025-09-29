// Problem ID: 2798
// Title: Chunk Array
// Runtime: 62 ms

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let start = 0;
    let l = [];
    while (start < arr.length){
        let temp = [];
        let end = start+size;
        while (start < arr.length && start < end){
            temp.push(arr[start]);
            start+=1;
        }
        l.push(temp);
    }
    return l;
};
