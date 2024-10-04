from hw03 import  *

sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
a = berry_finder(sproul)
print(a)