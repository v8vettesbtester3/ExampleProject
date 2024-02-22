from talker import Talker
def main():
    # This comment is an added line in the file.
    print ("This has been modified from the original code.")
    t = Talker()
    t.speak("Hi")
    t.speak("Hello way over there!",True)

if __name__ == "__main__":
    main()
