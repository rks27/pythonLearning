word = input("Write palendrome or other:")
lists = list(word)
or_list = list(word)
len_list = len(lists)
for i in range(int(len_list/2)):
    len_list = len_list - 1
    bubblesorting = lists[i]
    lists[i] = (lists[len_list])
    lists[len_list] = (bubblesorting)
a = "".join(lists)
if or_list == lists:
    print("P-p-palen-d-drome is nice and freezong like ding dong")
    print(" \" "+ word + " \" " + " is " + " \" " + a + " \" " + " backwards. ")
else:
    print("warm and sunny. no pale n dromes for today")
    print(word + " is " + a + " backwards ")
