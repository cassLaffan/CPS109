'''Write a program that reads the lyrics from the .txt 
into a list. Then, print off the elements of the list 
one at a time, with every fifth line intended with the 
tab character.'''

def read_lyrics(file):
    lyric_list = []
    with open(file, 'r') as f:
        for line in f:
            lyric_list.append(line)
    
    #counter = 1
    for lyric in range(len(lyric_list)):
        if (lyric + 1) % 5 == 0:
            print("\t", lyric_list[lyric], end="")
            #counter = 1
        else:
            print(lyric_list[lyric], end="")
            #counter = counter + 1

if __name__ == "__main__":
    read_lyrics("Season_Of_The_Witch.txt")