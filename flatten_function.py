""""
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, 
non-scalar verilerden de oluşabilir. 

Örnek olarak:
input : [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output: [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5 ]
"""""
sample_list = [ [1, 'a', ['cat'], 2], [ [[3]], 'dog'], 4, 5, {"bir":1, "iki":2 } ] 

def flatten_list(L):
    result = []    
    if type(L) == list or type(L) == tuple: 
        for e in L:
            result += flatten_list(e)     
    elif type(L) == dict:
        for i, j in L.items():
            result += (flatten_list(i) + flatten_list(j))
    else:
        result.append(L)
    return result       

print(f"Flattened Sample List: {flatten_list( sample_list )} ") 
# output ----------> [ 1, 'a', 'cat', 2, 3, 'dog', 4, 5, 'bir', 1, 'iki', 2]
