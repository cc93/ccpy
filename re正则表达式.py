import re

# match
print('\n方法re.match()：从头开始匹配，只要一开始匹配失败就会返回None')
def pMatch(pattern, string):
    """
print matched object
    :param pattern: [re.pattern]
    :param string: [str] string to be matched by re pattern
    """
    ma = pattern.match(string)
    if ma:
        print(ma.group())
    else:
        print('None of string "' + string + '" matched by pattern "' + pattern.pattern + '"')


# 匹配0-99
# ? 匹配0次或1次
pat = re.compile(r'[1-9]?\d$')
pMatch(pat,'98')
pMatch(pat,'08')
pMatch(pat,'8')
pMatch(pat,'128')
pMatch(pat,'100')
pMatch(pat,'00')
pMatch(pat,'0')
pMatch(pat,'1a')
pMatch(pat,'a1')


# 非贪婪模式（尽可能少的匹配） *? or +? or ??
print(re.match(r'[0-9][a-z]+?', '1bc').group())

# 匹配指定次数 {m} 匹配m次 or {m,n} 匹配m到n次
s = 'hnlichong@qq.comqa'
print(re.match(r'[_\w]{6,15}@qq.com', s).group())
s = 'chong@qq.com'
pMatch(re.compile(r'[_\w]{6}@qq.com'), s)

# 匹配有效变量名
list = ['_12', '12a', 'aAttack', 'a_attack', 'a-attack', '_']
for i in list:
    pMatch(re.compile(r'[_a-zA-Z]+[_\w]*'), i)
    # \w 匹配单词字符[a-zA-Z0-9]
    # + 匹配1次或多次
    # * 匹配0次或多次

# 边界匹配
# ^ $ 匹配开头，结尾
list = ['%hnlichong@qq.com', 'hnlichong@qq.comqa', 'hnlichong@qq.com']
for i in list:
    pMatch(re.compile(r'^[_\w]{6,15}@qq.com$'), i)
# \A \Z 匹配指定的开头字符串，结尾字符串
pMatch(re.compile(r'^\Aimooc[_\w]{1,10}@qq.com$'), 'imooc@qq.com')
pMatch(re.compile(r'^\Aimooc[_\w]{1,10}@qq.com$'), 'imooci@qq.com')
pMatch(re.compile(r'^\Aimooc[_\w]{1,10}@qq.com$'), 'iimooc@qq.com')
pMatch(re.compile(r'^\Aimooc[_\w]{1,10}@qq.com$'), 'ihnlichong@qq.com')

# 分组匹配
# | 或
# () 表示一个分组
pMatch(re.compile(r'^[_\w]{6,15}@(qq|163|126).com$'), 'hnlichong@qq.com')
pMatch(re.compile(r'^[_\w]{6,15}@(qq|163|126).com$'), 'hnlichong@163.com')
pMatch(re.compile(r'^[_\w]{6,15}@(qq|163|126).com$'), 'hnlichong@110.com')
# \1 引用第1个分组匹配到的字符串
pat = re.compile(r'<([_\w]+)>.+</\1>')
# .匹配任意单个字符，包括空格
pMatch(pat, '<book>A New Life</book>')
pMatch(pat, '<book>A New Life</ebook>')
pMatch(pat, '<book>A New Life<book>')
pMatch(pat, '<book>A-Man</book>')
pMatch(pat, '<book></book>')


# search
print('\n方法re.search(): 查找一次')
s = 'JavaScript: 3个月，Nodejs和MongoDB：1个月，Java和安卓开发：3个月'
pat = re.compile(r'\d+')
mat = pat.search(s)
print(mat.group())

# findall
print('\n方法re.findall(): 查找所有')
s = 'JavaScript: 3个月，Nodejs和MongoDB：1个月，Java和安卓开发：3个月'
pat = re.compile(r'\d+')
mat = pat.findall(s)
print(mat)

# sub
def add1(match):
    val = int(match.group())
    val+=2
    return str(val)
print('\n方法re.sub(): 替换')
s = 'age = 23'
pat = re.compile(r'\d+')
res = pat.sub(add1,s)
print('res = '+ res)

# split
print('\n方法split: 按匹配的字符符号分割')
s = 'imooc: Java C++, JavaScript|Python'
# 分割的字符符号有 冒号+空格，冒号，空格，逗号+空格，逗号，分隔号，空格+分隔号+空格 七种
pat = re.compile(r': |:| |, |,|\|| \| ')
res = pat.split(s)
print('res = ' + str(res))