(define (deep-map fn s)
  (if (null? s)
      '()
      (if (list? (car s))
          (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
          (cons (fn (car s)) (deep-map fn (cdr s))))))
