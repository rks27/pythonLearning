for i in  ("Andy", "Bob", "Jack", "Sam"):
    for j in  ("Andy", "Bob", "Jack", "Sam"):
        for k in  (" Andy", " Bob", "Jack", "SAm"):
            for l in  (" Andy", " Bob", "Jack", "Sam"):
                if i != j:
                    if i != k:
                        if j != k:
                            if j != l:
                                if k != l:
                                    print("________________________________")
                                    print(i, j, k, l)
            
                   
                   
