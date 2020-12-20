# 这是一些关于PYTHON编程的联系，你可以直接在题目后面写出代码。
import string
# 1. 找出下面两个数组的公共部分并打印出来
# a = [1, 1, 2, 3, 5, 8, 15, 21, 34, 56, 86]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

a = [1, 1, 2, 3, 5, 8, 15, 21, 34, 56, 86]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
intersect = []
for element in b:
    if element in a:
        intersect.append(element)
print(intersect)
#
# 2. 将数组里重复的数字除去。打印出最后结果。
# list1 = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14]
list1 = [1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14]
set1 = set(list1)
print(set1)
#
# 3. 统计下面的数列，用MAP格式打印出各个水果有几个。
# fruit = ['apple', 'pear', 'mango', 'banana', 'banana', 'pear', 'apple', 'mango', 'banana']
fruit = ['apple', 'pear', 'mango', 'banana', 'banana', 'pear', 'apple', 'mango', 'banana']
fruit_set = set(fruit)
fruit_dict = dict()
for i in fruit_set:
    fruit_dict[i] = fruit.count(i)
print(fruit_dict)
#
# 4. 在test项目目录中打开一个名为test.txt的文件，在已有文字后面，写入"hello world"。如果找不到文件，本地创建一个同名新文件。
f = open("test.txt", "a")
f.write("hello world")
f.close()
#
# 5. 用户指定一个数列，可以将1-10内数字英文单词变换成相应数字， 例如 [one, three, two, five, six] -> [1, 3, 2, 5, 6]
to_num: Dict[str, int] = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                          'nine': 9, 'ten': 10}
eng_num = []
n = int(input("Please enter number of elements in the list: "))
for i in range(0, n):
    elem = str(input())
    eng_num.append(to_num.get(elem))
print(eng_num)


# 6. 将给定数组里的数，分成奇数和偶数两个数列，分别打印出来。例如 [1,3,4,5,7,8,9,11,20] -> [1,3,5,7,9,11] [4,8,20]
def even_odd(arr):
    even = []
    odd = []
    for j in arr:
        if j % 2 == 0:
            even.append(j)
        else:
            odd.append(j)
    print(even)
    print(odd)


array6 = []
n = int(input("Please enter number of elements in the list: "))
for i in range(0, n):
    elem = int(input())
    array6.append(elem)
print(array6)
even_odd(array6)
#
# 7. 给定一段话，找出最高频的那个单词。例子中的 music.
text7 = "hey guys bla bla bla"
array7 = text7.split()
max_ct = 0
max_ind = 0
for elem7 in array7:
    if array7.count(elem7) > max_ct:
        max_ct = array7.count(elem7)
        max_ind = array7.index(elem7)
print(array7[max_ind])

# 8. 按照数字大小顺序排列 ["1","11","3","22","32","4","2","201"]
array8 = ["1", "11", "3", "22", "32", "4", "2", "201"]
to_int = []
for elem8 in array8:
    to_int.append(int(elem8))
to_int.sort()
arr8 = [str(ele8) for ele8 in to_int]
print(arr8)
