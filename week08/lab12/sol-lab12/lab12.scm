(define (no-repeats s)
  (if (null? s)
      s
      (cons (car s)
            (no-repeats
             (filter (lambda (x) (not (= (car s) x))) (cdr s))))))

(define (without-duplicates lst)
  (if (null? lst)
      lst
      (cons (car lst)
            (without-duplicates
             (filter (lambda (x) (not (= (car lst) x)))
                     (cdr lst))))))

(define (reverse lst)
  (if (null? lst)
      nil
      (append (reverse (cdr lst)) (list (car lst)))))
