from pprint import pprint

str1 = "hello there sasjdb jhebfv jabhsf uwfg shmdb hjcf hm hb shd bhhvbsdj hsdf sdf"
str2 = "cfskh ef hello tjhds there lsdfi ndsuh hdeu nhvfhi sefbh shd vkdlf"

arr1 = str1.split(" ")
arr2 = str2.split(" ")

n1 = len(arr1)
n2 = len(arr2)

dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

for i in range(n1):
  for j in range(n2):
    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    if arr1[i] == arr2[j]:
      dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])
    pprint(dp)

pprint(dp)

print(arr1, arr2)