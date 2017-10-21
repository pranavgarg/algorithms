;; Find a reversed / inverted fibonacci of `n`, given an `upper` bound.
;; examples
;; (fib 10) => 55,
;; (rev-fib 0 10) => 55,
;; (fib 4) => 3,
;; (rev-fib 6 10) => 3

(define (reverse-fib n upper)
  (define inverse-n
    ; handle edge cases of n
    (if (and (< n upper) (> n 0))
	(- upper n)
	0))
  (define (fib n)
    (cond ((= n 0) 0)
	  ((= n 1) 1)
	  (else (+ (fib (- n 1)) (fib (- n 2))))))
  (fib n'))
