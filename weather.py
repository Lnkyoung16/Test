A = ["a", "b", "c"]
B = ["a", "b", 3, "d", "e"]

# print(B[3])
#
# print(len(B))

def show_list(var1, index_num):
    for v in range(0,len(var1)):
        if v != index_num:
            print (var1[v])

show_list(A, 0)


