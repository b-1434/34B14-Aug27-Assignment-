#Binary search with random test cases

pos=-1

def search(list,n):

    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False



list=[]
k=int(input("enter number of elements: "))

for i in range(0,k):
    ele=int(input("Enter the numbers in list: "))
    list.append((ele))
n=int(input("Enter the number to search: "))

if search(list,n):
    print("found at",pos+1)
else:
    print("not found")
    
    Output:-
    #TEST 1
 enter number of elements: 4
Enter the numbers in list: 1
Enter the numbers in list: 2
Enter the numbers in list: 3
Enter the numbers in list: 4
Enter the number to search: 3
found at 3

#TEST2

enter number of elements: 5
Enter the numbers in list: 1
Enter the numbers in list: 5
Enter the numbers in list: 7
Enter the numbers in list: 8
Enter the numbers in list: 91
Enter the number to search: 91
found at 5

#TEST3

enter number of elements: 3
Enter the numbers in list: 1
Enter the numbers in list: 2
Enter the numbers in list: 5
Enter the number to search: 2
found at 2
