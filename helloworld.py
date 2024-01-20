import datetime


def display_hello_jeetu():
    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Format the date, time, and year
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")
    year = current_datetime.year

    # Display the heading and information
    print("HELLO JEETU")
    print("Today's Date:", formatted_date)
    print("Current Time:", formatted_time)
    print("Current Year:", year)


# Call the function to display information
display_hello_jeetu()
