def linear_search():
    a = list(map(int,input("\n\t\t\tEnter the elements: ").split()))
    num = int(input("\n\t\t\tEnter the number to search: "))
    for i in a:
        if i == num:
            print("\n\t\t\t{} found at index {}\n{}".format(num,a.index(i)+1,'='*80))
            break
    else:
        print("\n\t\t\t{} doesn't exist\n{}".format(num,'='*80))
    
# linear_search()

class BinarySearch:
    def binary_search(self,a,first,last,num):
        if first <= last:
            mid = (first+last)//2
            if a[mid] == num:
                print("\n\t\t\t{} found at location: {}\n{}".format(num, mid+1,'='*80))
                return 1
            elif a[mid] > num:
                return self.binary_search(a, first, mid-1,num)
            elif a[mid] < num:
                return self.binary_search(a, mid+1, last,num)
        return -1
    def call(self):
        a = list(map(int,input("\n\n\t\t\tEnter the elements in sorted order: ").split()))
        num = int(input("\t\t\tEnter the number to search: "))
        result = self.binary_search(a,0,len(a)-1,num)
        if result == -1:
            print("\n\t\t\t{} not found\n{}".format(num,'='*80))
    
# BinarySearch().call()

def invalid():
   print("INVALID CHOICE!")

def breaking():
    print("\t\t\n\n\n"+ 80* '=' + "\n\n\n\t\t\tThanking You\n\n\n",80*'=')
    pass

print("\n\n\n\n", 70*'-',"\n\n")


while(True):
    menu = {"1" : ('Linear Search',linear_search),
        "2" : ('Binary Search',BinarySearch().call),
        "3" : ('Exit', breaking)
        }
    for key in menu.keys():
         print("\t\t\t" + key + "-> " + menu[key][0])
         
    print("\n\n\n", 70*'-')

    ans = input("\n\n\t\t\tMake A Choice: ")
    menu.get(ans,(None,invalid))[1]()

    ch = input("Do You want to continue (Y/N): ")
    if ch == 'Y' or ch == 'y':
        continue
    else:
        break
