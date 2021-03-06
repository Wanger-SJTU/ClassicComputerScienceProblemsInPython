
# 汉诺塔问题

>汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。
![image](https://wx4.sinaimg.cn/large/6b71d347ly1g14l6ea8d4j20a503ujr6.jpg)


从左到右有A、B、C三根柱子，其中A柱子上面有从小叠到大的n个圆盘，现要求将A柱子上的圆盘移到C柱子上去，期间只有一个原则：一次只能移到一个盘子且大盘子不能在小盘子上面，求移动的步骤和移动的次数。

| n | 步骤 | 次数（sum） |
| ------ | ------ | ------ |
| 1 | 第1次  1号盘  A---->C  | 1 次   |
| 2 | 第1次  1号盘  A---->B  |        |
|   | 第2次  2号盘  A---->C  |        |   
|   | 第3次  1号盘  B---->C  |  3 次  |
|3  | 第1次  1号盘  A---->C  |        |
|   | 第2次  2号盘  A---->B  |        |
|   | 第3次  1号盘  C---->B  |        |  
|   | 第4次  3号盘  A---->C  |        |  
|   | 第5次  1号盘  B---->A  |        |  
|   | 第6次  2号盘  B---->C  |        |  
|   | 第7次  1号盘  A---->C  |  7次   |          

不难发现规律：
>1个圆盘的次数 2的1次方减1
2个圆盘的次数 2的2次方减1
3个圆盘的次数 2的3次方减1
。  。   。    。   。 
n个圆盘的次数 2的n次方减1
故：移动次数为：2^n - 1



>实现这个算法可以简单分为三个步骤：
> 1. 把n-1个盘子由 A 移到 B；
> 2. 把第n个盘子由 A 移到 C；
> 3. 把n-1个盘子由 B 移到 C；