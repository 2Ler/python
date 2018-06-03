import pickle
f = open("sample.txt","w")
pickle.dump(17,f)
x = pickle.load(f)
print x
print type(x)
