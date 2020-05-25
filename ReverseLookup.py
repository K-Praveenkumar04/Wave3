#ReverseLookup\
def reverseLookup(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
def main():
    antonyms = {"sad" : "happy", "left" : "right", "stop" : "go", "sweet" : "sour"}
    print("The antonym for 'sad' are: ", reverseLookup(antonyms, "sad"))
    print("happy")
    print()
    print("The antonym  for 'left' is: ", reverseLookup(antonyms, "left"))
    print("right")
    print("The antonym  for 'stop' is: ", reverseLookup(antonyms, "stop"))
    print("go")
if __name__ == "__main__":
    main()