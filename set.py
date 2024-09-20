setA={0,1,3,6,5,7,9}
setB={1,2,8,2,6,4,8}

setD=setA.difference(setB)
print(setD)

setSD=setA.symmetric_difference(setB)
print(setSD)

setU=(setA.union(setB))
print(setU)

setI=setA.intersection(setB)
print(setI) 