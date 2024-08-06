limit = int(input("Enter the limit "))
arm = []
not_arm = []
for i in range(limit):
    ele = int(input())
    temp = ele
    s = 0
    pw = len(str(ele))
    for j in range(1,temp+1):
        d = temp%10
        s+=d**pw
        temp = int(temp/10)
    if ele==s:
        arm.append(ele)
    else:
        not_arm.append(ele)
print(arm)
print(not_arm)
