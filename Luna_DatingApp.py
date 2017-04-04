#Luna Cuervo
#Program2


print("Hi there, let's see if you like the same things as this "
      "person and we will determine if you are match, just answer"
      " the questions and we will do the rest")
name=input("What is your name ")


animal=input("\n \n What is your favorite animal? ")

if ( "Cat" in animal or "cat" in animal) :
    print("\n \n You like the same animal!")
else:
    print("\n \n Oh sorry! You guys like different animals")

movie=input("\n \n What is your favorite movie? ")

if ("Clueless" in movie) :
    print(" You are a match!")
else:
    print("Oh, sorry you are not a match")


print(name, "f you matched for one or more you are meant to be, if not maybe you"
      " should try another person") 
    
