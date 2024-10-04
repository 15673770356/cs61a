(define (composed f g)
  (lambda (x)
    (f (g x))))

(define (repeat f n)
  (lambda (x)
    (define (repeat-helper f n x)
      (if (<= n 0)
          x
          (repeat-helper f (- n 1) (f x))))
    (repeat-helper f n x)))
