from itertools import chain


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


# итератор
class FlatIterator:

	def __init__(self, list):
		self.index = 0
		self.list = [a for b in list for a in b]

	def __iter__(self):
		return self

	def __next__(self):
		if self.index + 1 > len(self.list):
			raise StopIteration
		self.index += 1
		return self.list[self.index-1]

for item in FlatIterator(nested_list):
	print(item)


# 2 способ
new_list = [a for b in nested_list for a in b]
for item in new_list:
	print(item)


# 3 способ
new_list = list(chain.from_iterable(nested_list))
for item in new_list:
	print(item)


# генератор
def flat_generator(nested_list):
	for internal_list in nested_list:
		for value in internal_list:
			yield value

for item in flat_generator(nested_list):
	print(item)
