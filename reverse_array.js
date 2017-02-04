// O(N) runtime: Traversing through half the array doesn't matter.
'use strict';

// Reverse elements of an array
function reverse(arr) {
  for (let i = 0; i < arr.length / 2; i++) {

    // Traversing from the end backwards
    let other = arr.length - i - 1;

    // Going forward
    let temp = arr[i];

    // Swap the front element with the back element
    arr[i] = arr[other];

    // Swap the back element with the temp stored front element.
    arr[other] = temp;
  }
}

var arr = [1, 2, 3, 4, 5];
reverse(arr);
console.log(arr);