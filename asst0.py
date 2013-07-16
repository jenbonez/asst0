def main():
    fname = raw_input("What is your first name, yopro? ")
    lname = raw_input("What is your last name, %s? " % fname)
    print "Hello " + fname + " " + lname


if __name__ == "__main__":
    main()
