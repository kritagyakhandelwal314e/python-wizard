import re
# regex101.com
pattern = re.compile(r'this[a-z]*')
string = 'search inside this text please! thisalso'

print(pattern.search(string))
a = pattern.search(string)
print(a.span())
print(a.group())
b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)
print(pattern.match(string))


