(define (duplicate lst)
  (if (null? lst)
      '()
      (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))
