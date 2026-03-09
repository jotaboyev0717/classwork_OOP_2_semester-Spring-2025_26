class UserAccount:
    def __init__(self, username, email, password):
        self._username = username
        self.email = email
        self.__password = password
        
    @property
    def username(self):
        return self._username
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if value.count('@') != 1:
            raise ValueError("Invalid email address")
        self._email = value
        
    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            raise ValueError("Incorrect password")
        if len(new_password) < 6:
            raise ValueError("Password must be at least 6 characters")
        self.__password = new_password
    
    def login(self, password):
        if self.__password == password:
            return True
        else:
            return False
    def display_info(self):
        return f"{self._username} ({self._email})"
    
u = UserAccount("alisher", "alisher@mail.com", "secret123")
print(u.username)
print(u.email)
print(u.display_info())

print(u.login("wrong"))
print(u.login("secret123"))

u.email = "new@email.com"
print(u.display_info())

u.change_password("secret123", "newpass456")
print(u.login("secret123"))
print(u.login("newpass456"))

try:
    u.change_password("wrong", "abc123")
except ValueError as e:
    print(e)

try:
    u.change_password("newpass456", "short")
except ValueError as e:
    print(e)

try:
    u.email = "invalid-email"
except ValueError as e:
    print(e)

try:
    u.username = "hacker"
except AttributeError:
    print("Cannot change username")

try:
    print(u.__password)
except AttributeError:
    print("Cannot access private password")