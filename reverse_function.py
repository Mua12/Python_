"""
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 

Örnek olarak:
input : [[1, 2], [3, 4], [5, 6, 7]]
output: [[7, 6, 5], [4, 3], [2, 1]]
"""
sample_list = [[1, 2], [3, 4], [5, 6, 7]]                     

def reversed_list ( i_list):                                                  
    return( [ el[::-1] for el in i_list ][::-1] )                                                          
                                                              
print(f"Reversed Sample List: { reversed_list ( sample_list ) }") 
# output ----------> [[7, 6, 5], [4, 3], [2, 1]]