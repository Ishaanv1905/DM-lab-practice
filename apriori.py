#from itertools import combinations
transactions = [
    {'A', 'B', 'E'},
    {'B', 'D'},
    {'B', 'C'},
    {'A', 'B', 'D'},
    {'A', 'C'},
    {'B', 'C'},
    {'A', 'C'},
    {'A', 'B', 'C', 'E'},
    {'A', 'B', 'C'}
]

min_support = 2
min_confidence = 0.6
# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def get_support(itemset):
    count = 0
    for t in transactions:
        if itemset.issubset(t):
            count += 1
    return count

def generate_candidates(prev_l, k):
    candidates = set()
    prev_list = list(prev_l)

    for i in range(len(prev_list)):
        for j in range(i + 1, len(prev_list)):
            union = prev_list[i] | prev_list[j]
            if len(union) == k:
                candidates.add(frozenset(union))

    return candidates


# -----------------------------
# APRIORI ALGORITHM
# -----------------------------

def apriori():
    # Step 1: C1
    items = set()
    for t in transactions:
        items |= t

    c1 = set([frozenset([i]) for i in items])

    l = []
    support_data = {}

    # L1
    l1 = set()
    for item in c1:
        sup = get_support(item)
        if sup >= min_support:
            l1.add(item)
            support_data[item] = sup

    l.append(l1)

    k = 2

    while l[k - 2]:
        ck = generate_candidates(l[k - 2], k)
        lk = set()

        for item in ck:
            sup = get_support(item)
            if sup >= min_support:
                lk.add(item)
                support_data[item] = sup

        if not lk:
            break

        l.append(lk)
        k += 1

    return l, support_data

l, support_data = apriori()

print("Frequent Itemsets:")
for i, level in enumerate(l):
    print(f"L{i+1}:")
    for item in level:
        print(set(item), "->", support_data[item])
