import random

class Location:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def display_info(self):
        return f"{self.city}, {self.country}"

class Account:
    def __init__(self, username, displayname, birthday, location):
        self.username = username
        self.displayname = displayname
        self.birthday = birthday
        self.location = location  # Location instance

    def display_info(self):
        location_info = self.location.display_info() if self.location else "Location not specified"
        return (
            f"Username: {self.username}\n"
            f"Display Name: {self.displayname}\n"
            f"Birthday: {self.birthday}\n"
            f"Location: {location_info}"
        )

class StarredFriend:
    def __init__(self, friend_account, starred_date):
        self.friend_account = friend_account
        self.starred_date = starred_date

    def display_info(self):
        return (
            f"Friend: {self.friend_account.displayname}\n"
            f"Starred Date: {self.starred_date}"
        )

class Chat:
    def __init__(self, user_account, friend_account):
        self.participants = [user_account, friend_account]
        self.messages = []

    def add_message(self, sender, content):
        self.messages.append({"sender": sender, "content": content})

    def display_messages(self):
        return "\n".join(f"{message['sender']}: {message['content']}" for message in self.messages)

class UserAccount(Account):
    def __init__(self, username, displayname, email, password, birthday, location, user_id):
        super().__init__(username, displayname, birthday, location)
        self.email = email
        self.password = password
        self.user_id = user_id
        self.friend_list = []

    def add_friend(self, friend):
        self.friend_list.append(friend)
        print(f"{friend.username} added to your friend list.")
        if isinstance(friend, UserAccount):
            chat_instance = Chat(self, friend)
            self.friend_list[-1].chat_instance = chat_instance  # Store the Chat instance in the Account
            print(f"Chat instance created between {self.username} and {friend.username} in CE_Tinder.")

    def star_friend(self, friend):
        if friend in self.friend_list:
            friend.starred = True
            print(f"{friend.displayname} starred.")

    def display_info(self):
        friend_list_info = "\nFriend List:\n" + "\n".join(
            f"{friend.display_info()} (Starred)" if getattr(friend, 'starred', False) else friend.display_info()
            for friend in self.friend_list)
        return f"User ID: {self.user_id}\nEmail: {self.email}\n{super().display_info()}{friend_list_info}"

class CE_Tinder:
    def __init__(self):
        self.user_accounts = []
        self.chats = []

    def make_user_profile(self, username, displayname, email, password, birthday, location, user_id):
        user_account = UserAccount(username, displayname, email, password, birthday, location, user_id)
        self.user_accounts.append(user_account)
        return user_account

    def try_add_friend(self, user_account, friend_account):
        if random.uniform(0, 100) <= 33.333:
            user_account.add_friend(friend_account)
            chat_instance = friend_account.chat_instance
            if chat_instance:
                self.chats.append(chat_instance)

# Example usage with default data:
ce_tinder = CE_Tinder()

user_location = Location("Cityville", "Countryland")
user_account1 = ce_tinder.make_user_profile(
    "john_doe", "John Doe", "john@example.com", "password123", "1990-01-01", user_location, "U123"
)

user_location2 = Location("Tech City", "Robonia")
user_account2 = ce_tinder.make_user_profile(
    "tech_guy", "Tech Guy", "tech@example.com", "techpass456", "1985-05-05", user_location2, "U456"
)

# Try adding friends with a 33.333% success rate
ce_tinder.try_add_friend(user_account1, user_account2)

# Star a friend
user_account1.star_friend(user_account2)

# Display information for user account
if ce_tinder.user_accounts:
    print("\nUser Account Information:")
    for account in ce_tinder.user_accounts:
        print(account.display_info())
