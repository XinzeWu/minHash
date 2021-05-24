data = np.array(data)
all_sig = []
for j in range(25): #采用25个签名
    lst = [i for i in range(200)]
    random.shuffle (lst)
    lst = np.array(lst)
    index = np.argsort(lst)
    sig = []
    for line in data:
        for i in range(200):
            if line[index[i]]==1:
                sig.append(lst[index[i]])
                break
    all_sig.append(sig)
