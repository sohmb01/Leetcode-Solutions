// Problem ID: 2746
// Title: Filter Elements from Array
// Runtime: 45 ms

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const ans = [];
    arr.forEach((element,index) => {
        if ( fn(element,index)) ans.push(element);
    });
    return ans;
};