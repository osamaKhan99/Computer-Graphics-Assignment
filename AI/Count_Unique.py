
def start():
    string_main ='I really want to do it but I cant'
    search_string ='I'
    main =string_main.split(' ')
    count(main ,search_string)
    unique(main)


def count(list ,search):
    occur =0
    for i in range(0 ,list.__len__()):
        if search == list[i]:
            occur+=1
        else:
            continue
    print(search ,' ' ,occur)

def unique(list):
    new_list =[]
    for i in range(0 ,list.__len__()):
        if list[i] not in  new_list:
            new_list.append(list[i])
    print(new_list)

if __name__ == '__main__':
    start()
