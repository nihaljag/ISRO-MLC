dT=1
def diff(a, k):
    return(a[k] - a[k-1])/dT

error = [1,2,3,4,5,7,7,8,9,10]

print(diff(error, 5))
print(error)
print([i for i in range(1,10)])