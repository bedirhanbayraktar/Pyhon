'''
class SortHelper:
    def __init__(self):
        pass
'''

def selection_sort(arry):
    for i in range(len(arry)):
        min_idx = i
        for j in range(min_idx + 1, len(arry)):
            if arry[j] < arry[min_idx]:
                min_idx = j

        arry[i], arry[min_idx] = arry[min_idx], arry[i]

    return arry

veriler = input("Lütfen sıralanması istediğiniz sayıları girin: ")
arry = [int(x) for x in veriler.replace(',', ' ').split()]
counts = {}
for num in arry:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

all_ones = True
for count in counts.values():
    if count != 1:
        all_ones = False
        break

if all_ones:
    print("Hepsinden 1 tane var.")
else:
    for num, count in sorted(counts.items()):
        print(f"{num} sayısından {count} tane var.")

print(selection_sort(arry))
