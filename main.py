nums1=[1,2,3,4,5]
nums2=[0,0,0,0,0]

def medians(nums1, nums2):
    s=sorted(nums1+nums2)
    if len(s)==0:
        m=s
    elif len(s) %2==1:
        m = s[len(s)//2]
    else:
        m= (s[len(s)//2] + s[len(s)//2 - 1]) /2
    return m

print(medians(nums1, nums2))
