import os
import time
import requests
from instabot import Bot
import colorama

# Initialize colorama for colored output
colorama.init()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear_screen()
    os.system("title Instagram Bot - Followers, Likes, and Views")
    
    bot = Bot()
    
    account_name = input("Enter your Instagram username: ")
    if not account_name:
        print("Error: Please input a valid username.")
        return

    response = requests.get(f"https://www.instagram.com/{account_name}/")
    if response.status_code != 200:
        print("Error: Instagram account not found.")
        return
    
    print("\nChoose a bot category:")
    print("[1] - Likes")
    print("[2] - Views")
    print("[3] - Followers")
    
    choice = input("> ")
    
    if choice == "1":
        url = input("Enter the Instagram post URL (public account required): ")
        if not url.startswith("https://www.instagram.com/p/"):
            print("Error: Invalid post URL.")
            return
        
        print("Liking the post...")
        bot.like(url)
        print("✅ Likes added successfully!")
    
    elif choice == "2":
        url = input("Enter the Instagram story URL (public account required): ")
        if not url.startswith("https://www.instagram.com/stories/"):
            print("Error: Invalid story URL.")
            return
        
        print("Viewing the story...")
        bot.view_story(url)
        print("✅ Views sent successfully!")
    
    elif choice == "3":
        print("Welcome to the Instagram Followers bot.")
        print("To access the follower generator, donate $5 via PayPal.")
        print("PayPal: https://paypal.me/InstaGenNtrx")
        
        transaction_confirmed = input("Enter 'yes' if you've completed the payment: ").strip().lower()
        
        if transaction_confirmed == "yes":
            print("Generating followers...")
            bot.follow(account_name)
            print("✅ Followers added successfully!")
        else:
            print("❌ Payment not verified. Followers bot is locked for 24 hours.")
    
    else:
        print("Error: Invalid selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
