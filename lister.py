mat =  [[1,2,3,4],[2,3,4,5], [3,4,5], [4,5], [5,1]]

def is_it_connected(mat):
    mat0 = mat[0]
    poss = mat0[1:]
    for n in poss:
        j = mat[n-1]
        w = j[1:]
        for wel in w:
            if wel not in poss:
                poss.append(wel)
    if set(poss) == set(list(range(1,len(mat)+1))):
        return True
    else:
        print(set(poss))
        print(set(list(range(1,len(mat)+1))))
        return False

print(is_it_connected(mat))
mat2 = [[1,2], [2,3,1], [3,2]]
mat3 = [[1,2], [2,1], [3]]

print(is_it_connected(mat2))
print(is_it_connected(mat3))