from time import sleep


while True:
    with open("aboba.txt", "w", encoding="utf-8") as file:
        file.write("aboba\n")
        sleep(5)
