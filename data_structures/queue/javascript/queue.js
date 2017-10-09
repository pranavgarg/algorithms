/* 
 * Pushing to a Queue takes O(1) runtime worst case.
 * Popping from a Queue takes O(1) runtime worst case.
 * Getting the size takes O(N) runtime.
 * Querying isEmpty takes O(1) runtime.
 *
 */
'use strict';

class Node {
    constructor(val) {
        this.val = val;
        this.next = undefined;
    }

    whoAmI() {
        return `Node ${this.val}`;
    }
}

class Queue {
    constructor() {
        this.head = undefined;
    }

    enque(val) {
        if (!this.head) {
            this.head = new Node(val);
            return;
        }

        let curr = this.head;

        while (curr.next) {
            curr = curr.next;
        }

        curr.next = new Node(val);
    }

    deque() {
        if (!this.head) {
            return;
        }

        let curr = this.head;
        this.head = curr.next;
        return curr;
    }

    isEmpty() {
        return !this.head;
    }

    size() {
        let count = 0;
        let curr = this.head;
        while (curr) {
            count += 1;
            curr = curr.next;
        }
        return count;
    }
}

// To test out, uncomment below ...
/*
var q = new Queue();
console.log(q);

q.enque("A");
q.enque("B");
q.enque("C");
console.log(q);
console.log(q.size());

q.deque();
console.log(q);
console.log(q.size());

console.log(q.isEmpty());
*/

module.exports.Node = Node;
module.exports.Queue = Queue;
