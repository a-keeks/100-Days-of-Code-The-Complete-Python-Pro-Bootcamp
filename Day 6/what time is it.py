t_24_clock = float(input("What time is it? "))

t_12_clock = t_24_clock - 12
t_12_clock = "{:.2f}".format(t_12_clock)


def my_function(time = t_24_clock):
    """Takes time from 24 hour closk and converts it into 12 hour clock"""
    if t_24_clock >= 24:
        print("This time doesn't make any sense")
    
    elif t_24_clock == 0:
        print("It is midnight.")
        
    elif 0 < t_24_clock < 12:
        print(f"It is {t_12_clock} in the morning.")
        
    elif t_24_clock == 12:
        print("It is noon.")
    
    elif 12 < t_24_clock < 24:
        print(f"It is {t_12_clock} in the afternoon.")

my_function(time=t_24_clock)                                                      