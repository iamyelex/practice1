# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    filename=".\story.txt"
    with open(filename) as y:
        read_file= y.read()
        print(read_file)


def count_words(filename):
    # [assignment] Add your code here
    filename = ".\story.txt"
    with open(filename) as y:
        read_file = y.read()
    read_split = read_file.split()

    count = {}
    for i in read_split:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

    
read_file_content('filename')
count_words("filename")