// Problem ID: 2858
// Title: Join Two Arrays by ID
// Runtime: 324 ms

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
   arr1.sort((x,y) => x.id - y.id);
   arr2.sort((x,y) => x.id - y.id);
   var merged = [];
   let i = 0, j =0;
   while (i<arr1.length && j<arr2.length){
       if (arr1[i].id < arr2[j].id){
           merged.push(arr1[i]);
           i+=1;
       }
       else if (arr1[i].id > arr2[j].id){
           merged.push(arr2[j]);
           j+=1;
       }
       else{
           merged.push({...arr1[i],...arr2[j]});
           i+=1;
           j+=1;
       }
   }

    while(i < arr1.length) {
        merged.push({...arr1[i]})
        i++
    }

    while(j < arr2.length) {
       merged.push({...arr2[j]})
        j++
    }
   return merged;
};