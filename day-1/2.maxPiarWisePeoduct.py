def max_pairwise_sum(a):
    max_product = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            max_product = max(max_product, a[i] * a[j])
    return max_product


print('input how many row you want: ')
n = int(input())
print('input the numbers with space: ')
x = input().split()
a = []
for i in range(len(x)):
    a.append(int(x[i]))

print('The Result is: ')
print(max_pairwise_sum(a))
