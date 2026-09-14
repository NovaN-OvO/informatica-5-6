from time import sleep
def main():
    playlist = ["Boston", "Dracula", "I Knew It, I Knew You", "hate that i made you love me", "Risk It All",]
    playlist.append("Be By You")
    print(playlist)
    print() #separator
    playlist.insert(0, "Bohemian Rhpasody")
    print(playlist)
    print() #separator
    playlist.pop(4)
    print(playlist)
    print()
    print(playlist.index("Risk It All")) #.index lets you know the index of a value
    print()
    print(f"Number of songs in the playlist: {len(playlist)}")
    print()
    playlist.reverse() #This method transforms the current list, it doesn't creates a new one
    print(playlist)
    print()
    playlist.sort()
    print(playlist)

    print()
    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song_played = playlist[0]
        playlist.pop(0)
        playlist.append(song_played)
        sleep(3) #if you typed "from time import sleep", you dont have to add "time." to make a method because it will only execute that specified method/function
        repeat -= 1
if __name__ == "__main__":
    main()
