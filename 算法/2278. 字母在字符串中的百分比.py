"""
给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
示例 1：

输入：s = "foobar", letter = "o"
输出：33
解释：
等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
示例 2：

输入：s = "jjjj", letter = "k"
输出：0
解释：
等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/percentage-of-letter-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def foo():
    import math
    s = "foobar"
    letter = "o"
    return math.floor(s.count(letter) / len(s) * 100)


print(foo())
