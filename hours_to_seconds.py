def hours_to_seconds(hours):
    seconds = hours * 60 * 60
    return seconds

def hours_to_min(hours):
    minutes = hours * 60
    return minutes

def test(hours):
    minutes = hours_to_min(hours)
    secs = hours_to_seconds(hours)
    print(f"{hours} hours is {minutes} minutes")
    print(f"{hours} hours is {secs} seconds")
    
hours = input("Please input Hours : ")
hours_int = int(hours)
test(hours_int)
