a={1,2,3,4}
b={3,4,5,6}

print("union:" +str(a|b))
print("intersection:" +str(a&b))
print("difference:" +str(a-b))
print("symmetric difference:" +str(a^b))
print('Are A and B disjoint?', a.isdisjoint(b))
