// Implement a stack using a single Queue.
// Push is an O(1) runtime.
// Pop is an O(N-1) or O(N) runtime (needs to recycle N-1 element each pop).
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
    this.q = new queue.Queue();
    this.last = undefined;
  }

  push(val) {
    this.q.enque(val);

    if (!this.last) {
      // Last in stack is the first and only in queue
      this.last = this.q.head;
      return;
    }

    this.last = this.last.next;
  }

  size() {
    return this.q.size();
  }

  pop() {
    let originalSize = this.size();
    for (let i = 0; i < originalSize; i++) {
      let node = this.q.deque();
      //console.log(i, node.val);
      //console.log(`head [${this.q.head.val}] & last [${this.last.val}]`);
      if (i == originalSize - 1) {
        //console.log(node.val);
        return node;
      }
      this.push(node.val);
    } 
  }
}

// Test it out ...
/*
var stack = new Stack();

var vals = ['a', 'b', 'c', 'd'];
for (let val of vals) 
  stack.push(val);


var d = stack.pop();
console.log(d.whoAmI());
var c = stack.pop();
console.log(c.whoAmI());
var b = stack.pop();
console.log(b.whoAmI());
*/