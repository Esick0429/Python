# def moon_weight(weight, increase):
#  for year in range(1, 16):
#     weight = weight + increase
#     moon_weight = weight * 0.165
#     print('第 %s 年是 %s' % (year, moon_weight))
# moon_weight(40, 0.5)


# def moon_weight(weight, increase, years):
#  years = years + 1
#  for year in range(1, years):
#     weight = weight + increase
#     moon_weight = weight * 0.165
#     print('第 %s 年是 %s' % (year, moon_weight))
# moon_weight(35, 0.3, 5)


import sys
def moon_weight():
 print('输入你的体重')
 weight = float(sys.stdin.readline())
 print('请问你每年增加的体重为：')
 increase = float(sys.stdin.readline())
 print('请输入要查询的年数')
 years = int(sys.stdin.readline())
 years = years + 1
 for year in range(1, years):
    weight = weight + increase
    moon_weight = weight * 0.165
    print('第 %s 年是 %s' % (year, moon_weight))
moon_weight()