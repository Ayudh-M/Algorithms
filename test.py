class BreakRecursion(Exception):
    def __init__(self, size):
        self.size = size
    pass

def MaxClique(M, S, k, n):
    if k == n:
        for i in range(n): 
            for j in range(n):  
                if S[i] == True and S[j] == True and i != j and M[i][j] == 0:
                    return float('-inf')
        
        size = 0
        for i in range(n):  
            if S[i] == True:
                size += 1
        if size == n:
            raise BreakRecursion(size)
        return size
    else:
        best = float('-inf')

        S[k] = True  
        best = max(best, MaxClique(M, S, k+1, n))
        S[k] = False  
        best = max(best, MaxClique(M, S, k+1, n))

        return best

# def main():
#     try:
#         M = [
#         [0, 1, 0, 1, 1, 0, 1, 0, 0],
#         [1, 0, 1, 0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 1, 0, 1, 0, 0],
#         [1, 1, 1, 1, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [1, 0, 0, 1, 1, 0, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0, 1, 0]
#         ]
#         S = [False,False,True,False,False,True,False,False,False]
#         #S = [True,True,False,False,False,False,False,False,False]
#         print(MaxClique(M,S,1,9))    

#     except BreakRecursion as e:
#         print("recursion broken, max clique found early:" + e.size)

def main():
    try:
        M = [
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0],
        ]
        S = [False,False,True,False,False,True,False,False,False]
        #S = [True,True,False,False,False,False,False,False,False]
        print(MaxClique(M,S,0,9))    

    except BreakRecursion as e:
        print(e.size)
main()
