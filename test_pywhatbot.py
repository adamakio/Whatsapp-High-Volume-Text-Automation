from pywhatbot import PyWhatBot

if __name__ == "__main__":
    msg1 = ["blah///blah"]
    msg2 = [r"C:/Users/zouha/OneDrive/Pictures/Density contour.jpg", "density contour"]
    msg3 = ["lol soy roboto"]
    msg_list = [msg1, msg2, msg3]
    numbers = ["+34663577786", "+16476176315"]
    bot = PyWhatBot(8, 3)
    while True:
        input("Press enter  to send")
        try:
            bot.send_message_to_numbers(numbers, msg_list)
        except Exception as e:
            print(e)
