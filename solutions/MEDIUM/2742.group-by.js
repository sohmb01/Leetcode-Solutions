// Problem ID: 2742
// Title: Group By
// Runtime: 117 ms

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let groupedList = {};
    this.forEach(x => {
        if (groupedList[fn(x)]){
            groupedList[fn(x)].push(x);
        }
        else{
            groupedList[fn(x)] = [x];
        }
    });
    return groupedList;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */