num_list = []
sum = 0

for _ in range(5):
    num = int(input())
    sum += num
    num_list.append(num)

num_list.sort()

print(sum // 5)
print(num_list[2])