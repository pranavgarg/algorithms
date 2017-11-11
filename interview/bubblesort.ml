open Printf

let rec bubble_up l =
  match l with
  | [] -> l
  | h :: t ->
     match t with
     | [] -> l
     | m :: r ->
        if h < m then h :: bubble_up t
        else m :: bubble_up (h :: r)

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
          

        
  
