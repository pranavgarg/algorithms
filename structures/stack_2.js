// Implement a stack using two Queues.
// Push is an O(1) runtime.
// Pop is an O(2N - 1) or O(N) runtime. 
// (Dequeuing q1 N-1 time, Enqueing q2 N-1 time, then swap two queues ).
// Space takes O(3) or O(1).
'use strict';

// ES6 --
// import { Node, Queue } from "queue";

// ES5 --
var queue = require('./queue');

class Node {
  constructor(val) {
    this.val = val;
  }

  whoAmI() {
    return `Node ${this.val}`;
  }
}

class Stack {
  constructor() {
    this.q1 = new queue.Queue();
    this.q2 = new queue.Queue();
  }

  push(val) {
    // Only push to q1
    this.q1.enque(val);
  }

  size() {
    return this.q1.size();
  }

  pop() {
    let q1Size = this.size();

    for (let i = 0; i < q1Size; i++) {
      let node = this.q1.deque();

      if (i == q1Size-1) {
        // Swap two queues
        let temp = this.q1;
        this.q1 = this.q2;
        this.q2 = temp;
        return node;
      }

      this.q2.enque(node.val);
    } 
  }
}

// Test it out ...
/*
var stack = new Stack();

var vals = ['a', 'b', 'c', 'd'];
for (let val of vals) 
  stack.push(val);

console.log(stack);

var d = stack.pop();
console.log(d.whoAmI()); // Node d
var c = stack.pop();
console.log(c.whoAmI()); // Node c
var b = stack.pop();
console.log(b.whoAmI()); // Node b
var a = stack.pop();
console.log(a.whoAmI()); // Node a
*/

