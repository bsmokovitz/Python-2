imput = input("Enter a number or numbers: ")

led = ["###\n# #\n# #\n# #\n###", "  #\n  #\n  #\n  #\n  #", "###\n  #\n###\n#  \n###", "###\n  #\n###\n  #\n###", "# #\n# #\n###\n  #\n  #", "###\n#  \n###\n  #\n###", "###\n#  \n###\n# #\n###", "###\n  #\n  #\n  #\n  #", "###\n# #\n###\n# #\n###", "###\n# #\n###\n  #\n###"]

for i in imput:
    print(led[int(i)])
    print("\n")