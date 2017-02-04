// The key to this is to be careful with setting bounds!
// Binary search usually has O(log N) runtime
// i.e. it keeps dividing the problem set in half (N/2, N/4, N/8, ... )
// and O(N) space complexity (recursive stack).
'use strict';

// Return 'true' if dst is found, and 'false' otherwise.
function search(dst, arr) {

  arr.sort((a, b) => a-b);

  console.log("Finding", dst, "in", arr);

  if ((arr.length == 1) && (arr[0] !== dst))
    return false;

  var middlebound = Math.floor(arr.length / 2);

  if (dst == arr[middlebound]) {
    return true;

  if (dst < arr[middlebound]) {
    console.log("%d is to the left...", dst);
    let lowerbound = 0;
    let upperbound = middlebound;
    return search(dst, arr.slice(lowerbound, upperbound));
  } 
  else if (dst > arr[middlebound-1]) {
    console.log("%d is to the right...", dst);
    let lowerbound = middlebound;
    let upperbound = arr.length;
    return search(dst, arr.slice(lowerbound, upperbound));
  }
}

var dst = 90;
var nums = [1, 2, 6, 10, 90, 53, 12, 8, 78, 4];

var included = search(dst, nums);
console.log(included);
