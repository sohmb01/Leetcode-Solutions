// Problem ID: 2864
// Title: Is Object Empty
// Runtime: 55 ms

/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    for (var i in obj) {
        return false;
    }
    return true;
};