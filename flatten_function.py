""""
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, 
non-scalar verilerden de oluşabilir. 

Örnek olarak:
input : [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5 ]
"""""
sample_list = [ [1, 'a', ['cat'], 2], [ [[3]], 'dog'], 4, 5]

def flatten_list(i_list):
    def _flatten_list(i_list, r):    
        if type(i_list) is not list:
            r.append(i_list)
        else:
            for e in i_list:
                r += flatten_list(e)
        return r
    return _flatten_list(i_list, [])       

print(f"Flattened Sample List: {flatten_list( sample_list )} ") 
# output ----------> [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5]