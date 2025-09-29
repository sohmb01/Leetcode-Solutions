// Problem ID: 2747
// Title: Apply Transform Over Each Element in Array
// Runtime: 51 ms

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const returnedArray = [];
    arr.forEach((element,index) => {
        returnedArray[index] = fn (element,index);
    });
    return returnedArray;
};