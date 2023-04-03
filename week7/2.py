while True:
    str = input("Enter string (q) : ")
    if str == "q" or str == "Q":
        print("Çıkış yapıldı.")
        break
    elif str.lower() != str:
        print("Hepsi küçük harfli değil.")
    elif str.isalnum():
        print(str)
        print("-"*len(str))
