(* 
 * 
 * Reversing a binary tree is a simple recursive operation 
 * with the following: 
 * Base case: A leaf node is reached
 * Recursive: Swap the tree at every other node level
 *
 * This kind of problem can never be better and elegantly 
 * expressed than in ML and pattern-matching. 
 * 
 * Below are two implementations with each's reverse function.
 *)

type 'a binary_tree_1 =
  | Leaf of 'a
  | Tree of 'a binary_tree_1 * 'a binary_tree_1

let reverse_1 tree_1 =
  let rec aux tree_1' = 
    match tree_1' with
    | Leaf _ -> tree_1'
    | Tree (t1, t2) -> Tree (aux t2, aux t1)
  in aux tree_1

type 'a binary_tree_2 =
  | Empty
  | Node of 'a * 'a binary_tree_2 * 'a binary_tree_2

let reverse_2 tree_2 =
  let rec aux tree_2' =
    match tree_2' with
    | Empty -> tree_2'
    | Node (data, t1, t2) -> Node (data, aux t2, aux t1)
  in aux tree_2
