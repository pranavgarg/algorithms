;; Find a reversed / inverted fibonacci of `n`, given an `upper` bound.
;; Examples:
;; (fib 10) => 55,
;; (rev-fib 0 10) => 55,
;; (fib 4) => 3,
;; (rev-fib 6 10) => 3

(define (reverse-fib n upper)
  (define inverse-n
    (if (and (< n upper)
	     (> n 0))
	(- upper n)
	0))
  (fib 1 0 inverse-n))

(define (fib a b count)
  (if (= count 0)
      b
      (fib (+ a b) a (- count 1))))
