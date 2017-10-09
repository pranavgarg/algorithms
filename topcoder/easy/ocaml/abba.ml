(*
 * Write a function `can_obtain` to proof if a string `i` (init)
 * can be transformed to a string `t` (target) with the following 
 * condition:
 *
 * string `i` and `t` only consist of letter 'A' and/or 'B'
 * string `t` is longer or equal in length to `i`
 * two ways to get `i` to `t` are:
 * 
 * 1. concatenate 'A' to `i` or
 * 2. reverse and concatenate 'B' to `i`
 *
 * Examples (pseudocode):
 *
 * i = "AB", t = "AABBABB"
 * assert can_obtain(t, i) is true because
 * "AB" -> "BAB" -> "BABB" -> "BABBA" -> "BABBAA" -> "AABBABB"
 * (i -> do 2 -> do 2 -> do 1 -> do 1 -> do 2)
 *)

open Printf

let reverse text =
  let rec helper i = 
    if i >= String.length text then ""
    else ( helper (i + 1) ^ String.make 1 (text.[i]) )
  in helper 0

let rec can_obtain t i =
  if t = i then true
  else if String.length i >= String.length t then false
  else ( can_obtain t (i ^ "A") ) || ( can_obtain t ((reverse i) ^ "B") )

(* test out *)
let () =
  let (t, i) = ("AABBABB", "AB") in
  let result = can_obtain t i in
  printf (
      if result then "%s can be obtained from %s\n"
      else "%s cannot be obtained from %s\n"
    ) t i
  
