// Problem ID: 2859
// Title: Add Two Promises
// Runtime: 51 ms

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */

var addTwoPromises = async function(promise1, promise2) {

    const [val1,val2] = await Promise.all([promise1,promise2]);
    var promise = new Promise(resolve => setTimeout(()=> resolve(val1+val2),1));
    return promise;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */