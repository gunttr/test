from time import sleep


while True:
    with open("aboba.txt", "w", encoding="utf-8") as file:
        file.write("aboba\n")
        file.write("bebris\n")
        file.write("safsafas\n")
        sleep(5)
