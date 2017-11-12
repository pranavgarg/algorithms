(*
 * The Third Commandment (from the Little Schemer)
 * When building a list recursively, describe the first typical
 * element, and then `cons` it onto the natural recursion.
 *)

let rec bubble_up l =
  match l with
  | [] -> l
  | h :: t ->
     match t with
     | [] -> l
     | m :: r ->
        (* The first typical element is h *)
        if h < m then h :: bubble_up t
        (* The typical element is m, then bubble h up *)
        else m :: bubble_up (h :: r)

(* This acts as an auxiliary function to keep track of the recursion *)
let bubble_sort l =
  let rec aux n l = 
    if n = 1 then bubble_up l
    else aux (n - 1) (bubble_up l)
  in aux (List.length l) l
  
let () =
  assert (bubble_sort [1] = [1]);
  assert (bubble_sort [1; 2; 3] = [1; 2; 3]);
  assert (bubble_sort [2; 1; 7; 9; 3] = [1; 2; 3; 7; 9]);
  assert (bubble_sort [5; 4; 3; 2; 2; 1] = [1; 2; 2; 3; 4; 5]);
  
