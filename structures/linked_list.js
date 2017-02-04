'use strict';

// Node is an implementation of a singly-linked node.
class Node {
  constructor(value = "?") {
    this.value = value;
    this.next = undefined;
  }

  whoAmI() {
    return `Node ${this.value}`;
  }
}

// LinkedList is an implementation of a singly-linked list.
class LinkedList {
  constructor() {
    this.head = undefined;
  }

  add(val) {
    let temp = new Node(val);
    temp.next = this.head;
    this.head = temp;
  }

  search(val) {
    let head = this.head;
    let found = false;
    while (head) {
      if (head.value === val) {
        found = head;
        break;
      }
      head = head.next;      
    }
    return found;
  }

  // Iterator protocol
  *[Symbol.iterator]() {
    let curr = this.head;
    while (curr) {
      yield curr;
      curr = curr.next;
    }
  }

  delete(val) {
    let prev = undefined;
    let curr = this.head;
    let found = false
    while (curr) {
      if (curr.value === val) {
        found = true;
        break;
      }
      prev = curr;
      curr = curr.next;
    }
    if (found) {
      if (prev === undefined) {
        this.head = curr.next;
      } else {
        prev.next = curr.next;
      }
      return found
    }
    return found
  }

  size() {
    let count = 0;
    let head = this.head;
    while (head) {
      count += 1;
      head = head.next;
    }
    return count;
  }

  get(index) {
    let i = 0;
    let curr = this.head;
    while (i < index) {
      curr = curr.next;
      i += 1;
    }
    return curr;
  }

  reverse() {
    let prev     = undefined
      , nextNode = undefined
      , curr     = this.head;
    while (curr) {
      nextNode = curr.next;
      curr.next = prev;
      prev = curr;
      curr = nextNode;
    }
    this.head = prev;
    }

  peek() {
    return this.head.value;
  }

  whoAmI() {
    return `LinkedList ${this.head.value}`;
  }
}

// Test out
var a = new LinkedList();
a.add("D");
a.add("C");
a.add("B");
a.add("A");

console.assert(a.peek(), "A");
console.assert(a.whoAmI(), "LinkedList A");
console.assert(a.search("B"), !undefined);
console.assert(a.get(1).whoAmI(), "Node B");

for (var node of a) {
  console.log(node.value);
}



