#Lists, Tuples, and Sets
#https://www.youtube.com/watch?v=W8KRzm-HUcc

#Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
''''
nums = [1,3,4,5]
#i_nums = nums.__iter__()
i_nums = iter(nums)
#print(i_nums)
#print(dir(i_nums))
#print(dir(nums))
while True:
    try:
       item = next(i_nums)
       print(item)
    except StopIteration:
        break
    
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))
'''
'''
class MyRange:
    def __init__(self,first,end):
        self.value = first
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value  >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,5)
#for i in nums:
#    print(i)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
'''
'''
def My_range(start,end):
    current = start 
    while current < end:
        yield current
        current += 1
mynums = My_range(1,10)
#print(next(mynum))
#print(next(mynum))
#print(next(mynum))
for i in mynums:
    print(i)
        
'''
'''
#https://www.youtube.com/watch?v=C3Z9lJXI6Qw&t=0s
#Python Coding Problem: Creating Your Own Iterators
class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.word = self.sentence.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        index = self.index 
        self.index += 1
        return self.word[index]
my_sentences = Sentence('This is a test')
for word in my_sentences:
    print(word)
'''
#using generator
def setn(sentences):
    for word in sentences.split():
        yield word

my_sentences = setn('This is a test')

print(next(my_sentences))
print(next(my_sentences))
print(next(my_sentences))
print(next(my_sentences))