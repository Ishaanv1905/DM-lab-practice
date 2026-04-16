from itertools import combinations
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
min_support=2
min_confidence=0.6
def get_support(itemset):
    count=0
    for t in transactions:
        if itemset.issubset(t):
            count+=1
    return count
def generate_candidates(prev_l,k):
    candidates=set()
    prev_list=list(prev_l)
    for i in range(len(prev_list)):
        for j in range(1,len(prev_list)):
            union=prev_list[i]|prev_list[j]
            if len(union)==k:
                candidates.add(frozenset(union))
    return candidates

def apriori():
    items=set()
    for t in transactions:
        items|=t
    c1=set([frozenset([i]) for i in items])
    l=[]
    support_data={}
    l1=set()
    for item in c1:
        sup=get_support(item)
        if sup>=min_support:
            l1.add(item)
            support_data[item]=sup
    l.append(l1)
    k=2
    while(l[k-2]):
        ck=generate_candidates(l[k-2],k)
        lk=set()
        for item in ck:
            sup=get_support(item)
            if sup>=min_support:
                lk.add(item)
                support_data[item]=sup
        if not lk:
            break
        l.append(lk)
        k+=1
    return l,support_data

l,support_data=apriori()
print("Frequent itemsets")
for i,level in enumerate(l):
    print(f"Level:{i+1}")
    for item in level:
        print(set(item),"->", support_data[item])
        
def gen_rules(l,support_data):
    rules=[]
    for level in l[1:]:
        for itemset in level:
            for i in range(1,len(itemset)):
                for left in combinations(itemset,i):
                    left=frozenset(left)
                    right=itemset-left
                    conf=support_data[itemset]/support_data[left]
                    if conf>=min_confidence:
                        rules.append((left,right,conf))
    return rules

rules=gen_rules(l,support_data)
print("Rules")
for left,right,conf in rules:
    print(set(left), "->", set(right), "Confidence:", round(conf, 2))
    