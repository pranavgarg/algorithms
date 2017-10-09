(* Find out if a string is a palindrome *)
open Printf
   
let is_palindrome word =
  let len = String.length word in
  let (front, back) = (len / 2, len / 2 + 1) in 
  match word with
  |  "" -> false
  | _  -> 
     let rec test_symmetry is_sym (fptr, bptr) =
       if ( not is_sym || fptr >= front || bptr <= back ) then is_sym
       else test_symmetry ( word.[fptr] = word.[bptr] ) (fptr + 1, bptr - 1)
     in
     try test_symmetry true (0, len - 1)
     with Invalid_argument msg -> printf "%s\n" msg; false

                               
(* test palindrome *)               
let () =
  
  let palindromes = ["abba" ; "BABBAB"; "AvA"; "244AbbA442"] in
  assert ( List.for_all is_palindrome palindromes );

  let not_palindromes = ["aVA"; "not palindrome"; "CARc"] in
  assert ( not (List.for_all is_palindrome not_palindromes) )
