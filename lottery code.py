import webbrowser
import time
import random

# Set your post and profile URLs
post_url = 'https://www.instagram.com/p/CroBBAGN9Nl/'
profile_url = 'https://www.instagram.com/sell_tekk.de/'

# Set the path to the file to store the data
data_file = 'winners.txt'

# Define the function to generate a random winning number
def generate_win_number():
    return random.randint(1000, 9999)

# Explain the rules and how much time the user has to complete each action
print("Welcome to our Instagram contest!")
print("To participate, you need to share our post and follow our profile.")
print(f"You have {30} seconds to share the post and {30} seconds to follow our profile.")
print("Let's get started!\n")
time.sleep(20) # wait for 30 seconds

# Open the post URL in the user's default browser
webbrowser.open(post_url)

# Wait for the user to complete the action of sharing the post
print(f"You have {30} seconds to share the post.")
time.sleep(30) # wait for 30 seconds

# Check if the user has shared the post
# Replace this condition with your own condition
shared_post = True

if shared_post:
    # Open the profile URL in the user's default browser
    webbrowser.open(profile_url)
    
    # Wait for the user to complete the action of following the profile
    print(f"You have {30} seconds to follow our profile.")
    time.sleep(30) # wait for 30 seconds
    
    # Check if the user has followed the profile
    # Replace this condition with your own condition
    followed_profile = True
    
    if followed_profile:
        # Generate the winning number
        win_number = generate_win_number()
        print(f"Congratulations, your entry number for the contest is {win_number}.")
        print("We will announce the winners soon!")
        
        # Save the data to the file
        with open(data_file, 'a') as f:
            f.write(str(win_number) + '\n')
    else:
        print("Sorry, you did not complete all the actions required to participate in the contest.")
else:
    print("Sorry, you did not complete all the actions required to participate in the contest.")
