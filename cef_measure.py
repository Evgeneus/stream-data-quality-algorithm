def get_CEF(O, S):
    N = len(O)
    for i in range(N-1):
        print i, 'mis-capturable'
        if O[i] != S[i]:
            print i, 'capturable'
            if O[i+1] == S[i+1]:
                print i, 'captured'
        if O[i+1] != S[i+1]:
            print i, 'mis-captured'


    print N-1, 'mis-capturable'
    if O[N-1] != S[N-1]:
        print N-1, 'capturable'

if __name__ == '__main__':
    ground_truth = ['Wisc','Wisc','Wisc','Wisc','MSR']
    observed =     [None  , 'UW' , None ,'Wisc','Wisc']
    
    get_CEF(ground_truth, observed)
