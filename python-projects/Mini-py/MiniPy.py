def Customized_Find_Function(word,char):
    '''
	return list which contains the indexes of char in word
    '''
    return [index for index,value in enumerate(word) if value==char]
     

def Customized_Split_Function(string,char,option):
    '''
    when option is equal 1 then we split with char the first char in String that equal char
    when option is equal 0 then we split with char all chars in String that equal char
    '''
    list_indexed_with_char=Customized_Find_Function(string,char)
    list_for_splited = []

    if option == 0 :
        start=0
        for index,value  in enumerate(list_indexed_with_char) :
            list_for_splited.append(string[start : value])
            start=value+1
        list_for_splited.append(string[start : ])
        return list_for_splited
    elif option ==1:
        return [string[ : list_indexed_with_char[0]] ,string[list_indexed_with_char[0]+1 : ]]
   
   
# test   
string='Abo Khayria byslem 3lyk'
char='b'

print(Customized_Split_Function(string,char,0))