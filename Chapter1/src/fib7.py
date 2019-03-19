# fib7.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def matrix_pow(M, N):
    res = [[0 for _ in range(2)] for _ in range(2)]    
    for i in range(2):
        for j in range(2):
            tmp=0
            for k in range(2):
                tmp += M[i][k]*N[k][j]
            res[i][j] = tmp
    return res


def fib7(n: int) -> int:
    if n == 0: return n  # special case
    fib0: int = 0  # initially set to fib(0)
    fib1: int = 1  # initially set to fib(1)
    base = [[1,1],[1,0]]
    res  = [[1,0],[0,1]]
    while n > 0:
        # print(res)
        if n % 2 ==1:
            res = matrix_pow(res,base)
        base = matrix_pow(base,base)
        n = n//2
    fib_n = res[1][0]
    return fib_n


if __name__ == "__main__":
    print(fib7(10))

