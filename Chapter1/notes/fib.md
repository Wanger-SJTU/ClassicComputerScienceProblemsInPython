
斐波那契数列的通项公式为$ f(n)=f(n-1)+f(n-2)$
求第n项:

1. 递归
    利用上述公式由f(n)计算到f(0),存在大量重复计算。5.中的`lru`可以优化效率。
    [code](../src/fib2.py)
2. 动态规划
    bottom-up 计算，记录之前的状态可以减少运算
    [code](../src/fib3.py)
3. 空间复杂度优化
    因为`f(n)` 仅仅与 `f(n-1)` `f(n-2)` 两个有关，可以仅仅使用两个变量来完成历史计算。
    [code](../src/fib5.py)
4. 生成器模式
    `None`
    [code](../src/fib6.py)
5. lru_cache
    利用lru装饰函数，可以简化代码。详见与[LRU](https://wanger-sjtu.github.io/2019/03/16/lru-cache/)
    [code](../src/fib4.py)

6. 快速幂
    此方法可以将复杂度减少到$O(\lg n)$。斐波那契数列的递推形式可以写为：
    $$ 
\left[ \begin{array}{c}{F i b(n+1)} \\ {F i b(n)}\end{array}\right]=\left[ \begin{array}{ll}{1} & {1} \\ {1} & {0}\end{array}\right] \left[ \begin{array}{c}{F i b(n)} \\ {F i b(n-1)}\end{array}\right]
 $$
 进而有
 $$ 
\left[ \begin{array}{c}{F i b(n+1)} \\ {F i b(n)}\end{array}\right]=\left[ \begin{array}{ll}{1} & {1} \\ {1} & {0}\end{array}\right]^{n} \left[ \begin{array}{c}{F i b(0)} \\ {F i b(1)}\end{array}\right]
 $$
 因此可以用快速求幂的方法求解。
 [code](../src/fib7.py)
