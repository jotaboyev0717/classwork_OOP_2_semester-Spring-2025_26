class BatchIterator:
    def __init__(self, data_list, batch_size):
        self.data_list = data_list
        self.batch_size = batch_size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.data_list) == 0:
            raise StopIteration
        batch = self.data_list[:self.batch_size]
        self.data_list = self.data_list[self.batch_size:]
        return batch
        
class Batched:
    def __init__(self, data_list, batch_size):
        self.data_list = data_list
        self.batch_size = batch_size
        
    def __iter__(self):
        return BatchIterator(self.data_list, self.batch_size)

b = Batched([1, 2, 3, 4, 5, 6, 7], 3)

for batch in b:
    print(batch)

print('---')

for batch in b:
    print(batch)
