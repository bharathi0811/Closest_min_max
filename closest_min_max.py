array =list(map(int,input("Enter the array elements: ")))
def close_min_max(array):
    n = len(array)
    if n<=2:
        return n
    else:
        min_ = array[0]
        max_=array[0]
        for i in array:
            if i>max_:
                max_=i
            if i <min_:
                min_=i
        j_index=0
        max_index=array.index(max_)
        index_=0
        l=[]
        for j in array:
            index_ += 1
            if j ==min_:
                l.append(index_)
        lst=0
        for m in range(l[-1],max_index+2):
            lst+=1
        return lst

print(close_min_max(array))
