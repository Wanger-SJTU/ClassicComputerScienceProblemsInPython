原Repo是 **Classic Computer Science Problems in Python** 的源代码。电子书地址为 [URL](https://www.manning.com/books/classic-computer-science-problems-in-python)

[EN](./README_EN.md)

## Version and Packages
代码运行环境为`python 3.7`，鉴于python3.7的一些语法特性（data classes, advanced type hints, etc.），个别代码可能不能在其他版本python上顺利运行。相关的代码依赖项，可以在
[typing_extensions](https://github.com/python/typing/tree/master/typing_extensions) 包含. 可以通过安装 `typing_extensions` 来解决依赖问题。 
> `pip3 install typing_extensions` or `pip install typing_extensions`

## 中文Repo 内容

参照电子书内容以及提供的源代码，在每章的文件夹下有相应内容的介绍。

#### 进展
- [X] Chapter 1
    - [x] [斐波那契数列](./Chapter1/notes/fib.md)
    - [X] [Trivial compression](./Chapter1/notes/compression.md)
    - [X]  [加密解密](./Chapter1/notes/encryption.md)
    - [X] [$\pi$](./Chapter1/notes/pi.md)
    - [X] [汉诺塔](./Chapter1/notes/hanoi.md)
    
- [ ] Chapter 2




## License
All of the source code in this repository is released under the Apache License version 2.0. See `LICENSE`.

**注**：如果代码中数学公式无法显示，可以在chrome中安装插件--`MathJax Plugin for Github`