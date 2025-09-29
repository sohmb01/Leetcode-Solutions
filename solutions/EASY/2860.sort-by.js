// Problem ID: 2860
// Title: Sort By
// Runtime: 130 ms

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const swap = function(a,b){
        return (fn(a) < fn(b) ? -1 : 1);
    }
    return arr.sort(swap);
};