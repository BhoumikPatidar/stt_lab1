lst = [5, 5, 2, 4, 1, 6]


def mergesort(l):
  if len(l) > 1:
    mid = len(l) // 2
    l1 = l[:mid]
    l2 = l[mid:]
    mergesort(l1)
    mergesort(l2)

    i = j = k = 0
    while i < len(l1) and j < len(l2):
      if l1[i] <= l2[j]:
        l[k] = l1[i]
        k += 1
        i += 1
      else:
        l[k] = l2[j]
        k += 1
        j += 1

    while i < len(l1):
      l[k] = l1[i]
      i += 1
      k += 1

    while j < len(l2):
      l[k] = l2[j]
      j += 1
      k += 1


mergesort(lst)
print(lst)
