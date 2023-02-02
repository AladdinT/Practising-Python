def merge_the_tools(string, k):
    # your code goes here
    myls = list(string)
    lsOfls = []
    
    for i in range(k):
        #split the whole string to lists of the desired length k
        lsOfls.append( (myls[(i*k):((i*k)+k)] )   )
        
        for j in range(k):
            #convert to a string to take advantage of rfind function
            '''
            for some reason it just blasts 
            IndexError: list index out of range
            it did not even print a line before the j loop 
            '''
            
            indexed = "".join(lsOfls[i]).rfind((lsOfls[i])[j])
            
            #if the char is duplicated (found in another index)
            if indexed not in (j,-1):
                if (lsOfls[i])[j] != ' ':
                    #replace that index with a space
                    lsOfls[i][indexed] = " " 
        #remove all spaces 
        #save the final desired string in the list
        lsOfls[i] = ("".join(lsOfls[i])).replace(' ', '')
                
    #print the list
    for i in lsOfls:
        print( i )
     
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)