import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time is up!')

def focus_clock():
    print("Welcome to the Focus Clock!")
    while True:
        try:
            minutes = int(input("How many minutes do you want to focus for? "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    seconds = minutes * 60
    print("Starting focus timer for {} minutes...".format(minutes))
    countdown(seconds)

if __name__ == '__main__':
    focus_clock()
