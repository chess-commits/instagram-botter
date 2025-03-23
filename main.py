import os
import time
import requests
from instabot import likes, views, followers
import colorama

colorama.init()
os.system("title Instagram Followers, Likes, and Views Botter.")

def main():
    account_name = input("Account name? ")
    
    if account_name == "":
        print("Please input a real name.")
        return

    response = requests.get(f"https://www.instagram.com/{account_name}/")
    if response.status_code != 200:
        print("I didn't find your Instagram account.")
        return

    print("\nPlease choose a bot category:")
    print("[1] - Likes\n[2] - Views\n[3] - Followers")
    
    choose = input("> ")

    if choose == "1":
        url = input("Paste your Instagram post URL (your account must be public): ")
        if not url.startswith("https://www.instagram.com/p/"):
            print("Invalid post URL.")
            return
        
        accnum = 1
        while accnum <= 10:  # Set a limit to prevent infinite loops
            likes.like(url)
            accnum += 1
            print(f"{accnum} likes done.")

    elif choose == "2":
        url = input("Please input your story URL (must be public): ")
        if not url.startswith("https://www.instagram.com/stories/"):
            print("Invalid story URL.")
            return
        
        views.view(url)
        print("Views sent successfully!")

    elif choose == "3":
        print("Welcome to the Instagram Followers bot.")
        print("Please donate $5 to access the follower generator.")
        print("PayPal: https://paypal.me/InstaGenNtrx")

        # Simulated transaction check (replace with actual API if needed)
        transaction_confirmed = input("Enter 'yes' if you've completed the payment: ").strip().lower()
        
        if transaction_confirmed == "yes":
            print("Access granted. Generating followers...")
            followers.follow(account_name)
        else:
            print("Payment not verified. Followers bot is locked for 24 hours.")

    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
