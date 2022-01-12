(define (factorial x)
    (if (= x 0) 1
        (* x (factorial (- x 1)))))

;5.1
(define (concat a b)
    (if (null? a) b
        (cons (car a) (concat (cdr a) b)))
)

;5.2
(define (replicate x n)
    (if (= n 0) nil
        (cons x ( replicate x (- n 1))))
)

(define (uncompress s)
    (if (null? s) s
                (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))))


;错误的basecase nil 无法进行选取
(define (uncompress s)
    (if (= (cdr s) nil) (replicate (car (car s)) (car (cdr (car s))))
                (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))))
;错的原因~
scm> (cdr '((c 3)))
()
scm> (cdr (cdr '((c 3))))
Traceback (most recent call last):
 0	(cdr (cdr (quote ((c 3)))))
Error: argument 0 of cdr has wrong type (nil)
scm> (car (cdr '((c 3))))
Traceback (most recent call last):
 0	(car (cdr (quote ((c 3)))))
Error: argument 0 of car has wrong type (nil)
scm> 


