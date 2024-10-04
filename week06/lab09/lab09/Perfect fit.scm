; Return whether there are n perfect squares with no repeats that sum to total
; 因为是多个决策 ， 所以是使用树递归 
    (define (fit total n)
        (define (f total n k)
            (if (and (= n 0) (= total 0))
                #t                ;  base case 
            (if (< total (* k k)) ; 如果不符合要求 ，超出了 大小 ，直接跳出来 
                #f
            ;YOUR-CODE-HERE
                
            )))
        (f total n 1))

    (expect (fit 10 2) #t)  ; 1*1 + 3*3
    (expect (fit 9 1)  #t)  ; 3*3
    (expect (fit 9 2)  #f)  ;
    (expect (fit 9 3)  #f)  ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
    (expect (fit 25 1)  #t) ; 5*5
    (expect (fit 25 2)  #t) ; 3*3 + 4*4
