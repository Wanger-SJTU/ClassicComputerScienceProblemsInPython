
# 计算 pi

## 使用格雷戈里 - 莱布尼茨无穷级数
$$
\begin{aligned}
\pi = \frac{4}{1} - \frac{4}{3} + \frac{4}{5} + \cdots =\sum_{i=0}^{N}\frac{(-1)^i\times 4}{1+2i}
\end{aligned}
$$


## Nilakantha 级数

$$
\begin{aligned}
\pi &=  3 + \frac{4}{2*3*4} - \frac{4}{4*5*6} + \frac{4}{6*7*8} - \frac{4}{8*9*10} + \frac{4}{10*11*12} - \frac{4}{12*13*14}+\cdots \\
&=3+\sum_{i=1}^{N}\frac{-1^{i-1}\times4}{2i*(2i+1)*(2i+2)}
\end{aligned}
$$


## 采样法

![image](https://wx3.sinaimg.cn/large/6b71d347ly1g14h3ax2xmj20gc0f8q37.jpg)

## 随机数互质的概率
>两个随机正整数 $a,b$  互质的概率为 $\frac{6}{\pi^2}$ 。这一性质的证明过程如下:

> 1. 设两个数$u,v$互质的概率为$p$，则 $gcd(u,v)=d$  当且仅当 $d_u, d_v，gcd(\frac{u}{d}, \frac{v}{d})=1$。
>2. 因此，任两个数最大公约数为 $d$ 的概率为$p/d/d$ ，即 $\frac{p}{d^2}$。
>3. 在正整数集合上有 $p+p/4+p/9+\cdots=1$ 容易求得 $p=\frac{6}{\pi^2}$。