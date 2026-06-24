import time

def timer():
    try:
        time_in_seconds = int(input("Enter the time in seconds: "))
        if time_in_seconds < 1:
            print("Invalid time. Please enter a valid time.")
            return
        return time_in_seconds
    except ValueError:
        print("Invalid time. Please enter a valid time.")
        return None
    except Exception as e:
        print(f"An error occurred. {e}")
        return None

def main():
    seconds = timer()
    if seconds is not None:
       for i in range(seconds,0,-1):
           print(f"Time remaining: {i} seconds", end="\r")
           time.sleep(1)

       print("\nTime is up!")
       
    else:
        print("Invalid time. Please enter a valid time.")
        main()

main()