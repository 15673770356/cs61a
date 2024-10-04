; 完成将一个列表中的所有数字都加一的操作

(define s (list 1 2 3 4))

; 定义一个将数字加一的函数
(define (plus x)
  (+ x 1))  ; 这里使用 + 函数将 x 加 1

; 使用 map 函数将 plus 应用于列表 s 的每个元素
(map plus s)
