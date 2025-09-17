def binary_tranfer(num,size_of_bits):
     num_in_binary=[]
     for i in range(size_of_bits):
        if 2**(size_of_bits-1-i)<=num:
            num_in_binary.append(1)
            num-=2**(size_of_bits-1-i)
        else:
            num_in_binary.append(0)
     negetive_num_in_binary=[]
     for i in range(len(num_in_binary)):
        if num_in_binary[i]==0:
            negetive_num_in_binary.append(1)
        else:
            negetive_num_in_binary.append(0)
     negetive_num_in_binary[-1]+=1
     for i in range(len(negetive_num_in_binary)):
        if negetive_num_in_binary[-1-i]==2:
            negetive_num_in_binary[-1-i]=0
            negetive_num_in_binary[-2-i]+=1
     if negetive_num_in_binary[0]==2:
        negetive_num_in_binary[0]=0
     answer=0
     for i in range (len(negetive_num_in_binary)):
         answer+=negetive_num_in_binary[i]*(10**(len(negetive_num_in_binary)-1-i))
     print(answer)
binary_tranfer(int(input()),int(input()))
    
    
    
    
