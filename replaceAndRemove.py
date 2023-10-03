'''
Consider the following rules that are to be applied to an array of characters
1. Replace each 'a` with 2 'd'
2. remove each 'b' 
Write a program which takes as input an array of characters and remove each 'b' and replace
each 'a' with 2 'd's Along the array, interger value size which represent num of entries of array
that the operation is to be applied.

algo find numbers of 'a' and remove 'd' on forward iteration during count of 'a' from array
'''


def replaceAndRemove(arr,size):
    write_idx = 0 
    a_count = 0
    for i in range(0,size):
        if arr[i] != 'b':
            arr[write_idx] = arr[i] 
            write_idx +=1
        if arr[i] == 'a':
            a_count +=1

    
    current_idx = write_idx - 1 
    write_idx = current_idx + a_count 
    print("write_idx", write_idx,"current_idx", current_idx, "a_count",a_count)
    final_size = write_idx +1 # due to 0 index base
    while current_idx >=0:
        if arr[current_idx] == 'a':
            arr[write_idx], arr[write_idx -1] = 'd', 'd'
            write_idx -=2
        else:
            arr[write_idx] = arr[current_idx]
            write_idx -=1
        current_idx -=1
    return final_size ,arr





if __name__ == '__main__':
    arr = ['a','c','a','a','-','-','-']
    size , a = replaceAndRemove(arr,4)
    print(size,a)

