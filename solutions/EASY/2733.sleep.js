// Problem ID: 2733
// Title: Sleep
// Runtime: 53 ms

/**
 * @param {number} millis
 */
async function sleep(millis) {
    return new Promise(function(resolve){
        setTimeout(resolve,millis);
    });
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */