from instabot import Bot
import time
import random

# Create an instance of the Bot
bot = Bot()

try:
    # Login to Instagram
    bot.login(username="00000000000unknownyyyy", password="Jeet2004")

    # Introduce a random delay before performing actions
    time.sleep(random.randint(300, 600))  # Sleep between 5 to 10 minutes

    # Follow a user
    bot.follow('photograpy_jeet')

except Exception as e:
    print(f"Encountered an error: {e}")

    # Wait for 10 minutes before retrying if an error occurs
    time.sleep(600)  # Sleep for 10 minutes before retrying

finally:
    # Logout after the task is completed
    bot.logout()
