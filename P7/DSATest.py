'''
testing DSAhash.py
'''

import DSAhash

def main():
    ht = DSAhash.DSAHashTable(10)

    print(ht.hashArray)
    hashToCheck = ht.hashFunction(10)
    ht.put(10, "ten")
    ht.put(20, "twenty")
    ht.remove(20)
    ht.remove(10)
    for item in ht.hashArray:
        print(item.getState())

if __name__ == "__main__":
    main()