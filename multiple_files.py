import utils
mess=input("Please type your message\n")

messf= utils.flip(mess)
con= utils.count_letters(mess,"a")

print(f"Your encoded message is: {messf}{con}")
