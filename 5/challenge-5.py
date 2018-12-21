import pickle

with open("banner.p", "rb") as pickle_data:
    data = pickle.load(pickle_data)

for line in data:
    for char in line:
        print(char[0] * char[1], end="")
    print("\n")