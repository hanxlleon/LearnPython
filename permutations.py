# -*- coding: utf-8 -*-
#给定一个字符串，返回所有的排列组合


def permutations(s):
    if len(s) <= 1:
        return s
    r = []
    for i in range(len(s)):
        p = permutations(s[:i]+s[i+1:])
        for x in p:
            r.append(s[i]+x)
    return r


if __name__ == '__main__':
    print permutations('123')

    

