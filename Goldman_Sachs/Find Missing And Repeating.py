#Find Missing And Repeating
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        k=[]
        #code for getting the duplicate nunber
        for i in range(n):
            if arr[i]==arr[i+1]:
                k.append(arr[i])
                break
        #finding the missing number
        a=set(arr)
        b=len(a)
        m=b+1
        total = m*(m+1)//2
        miss=total-sum(a)
        k.append(miss)
        return k
    
