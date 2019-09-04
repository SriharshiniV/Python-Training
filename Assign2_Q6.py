x=(input("Enter a string"))


def words(x):
    x = x.split(' ')

    for word in x:
        print(len(word))

words(x)

