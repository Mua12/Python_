""""
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, 
non-scalar verilerden de oluşabilir. 

Örnek olarak:
input : [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5 ]
"""""
sample_list = [ [1, 'a', ['cat'], 2], [ [[3]], 'dog'], 4, 5] 

def flatten_list(L):
    def _flatten_list(L, result):    
        if type(L) is not list and type(L) is not tuple:
            result.append(L)
        else:
            for e in L:
                result += flatten_list(e)
        return result
    return _flatten_list(L, [])       

print(f"Flattened Sample List: {flatten_list( sample_list )} ") 
# output ----------> [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5]
