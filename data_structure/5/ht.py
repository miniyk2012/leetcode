
ht = {}

# key 增改删查都是O(1)
ht[10] = "123"  # O(1)
ht[10] = "1234" # O(1)
del ht[10]  # O(1)
10 in ht  # O(1)

# value   CRUD是O(n)
"1234" in ht.values()  # O(n)


