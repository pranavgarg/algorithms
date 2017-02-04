'use strict';

class Node {
  constructor(data) {
    this.data = data;
    this.left = undefined;
    this.right = undefined;
  }

  whoAmI() {
    return `Node ${this.value}`;
  }
}

class BST {
  constructor() {
    this.root = undefined;
  }

  insert(data) {
    let n = new Node(data);
    if (!this.root) {
      this.root = n;
      return
    }

    let curr = this.root;

    while (data !== curr.data) {
      if (data < curr.data) {
        if (!curr.left) {
          curr.left = n;
          break;
        }
        curr = curr.left;
      }
      if (data > curr.data){
        if (!curr.right) {
          curr.right = n;
          break;
        }
        curr = curr.right;
      }
    }
  }

  search(data) {
    if (!this.root) return;

    let curr = this.root;
    if (!curr) return;

    while (curr) {
      if (data === curr.data) {
        return curr;
      } 
      else if (data < curr.data) {
        curr = curr.left;
      } 
      else if (data > curr.data) {
        curr = curr.right;
      }
    }
  }

  inOrder(root) {
    let curr = root;

    if (curr) {
      this.inOrder(curr.left);

      console.log(curr.data);

      this.inOrder(curr.right);
    }
  }

  postOrder(root) {
    let curr = root;

    if (curr) {
      this.inOrder(curr.left);
      this.inOrder(curr.right);
      console.log(curr.data);
    }
  }

  preOrder(root) {
    let curr = root;
    if (curr) {
      console.log(curr.data);
      this.preOrder(curr.left);
      this.preOrder(curr.right);
    }
  }

}

var bst = new BST();

/* 
 * Insert data to create such tree ->
 *
 *           (10)
 *           /  \
 *         (5)  (20)
 *         / \    \
 *       (3) (6)  (40)
 *
 */

for (var num of [10, 5, 3, 6, 20, 15, 40]) {
  bst.insert(num);
}

console.log(bst.search(5));

// Couple ways to traverse-print elements
bst.inOrder(bst.root);
bst.postOrder(bst.root);
bst.preOrder(bst.root);





