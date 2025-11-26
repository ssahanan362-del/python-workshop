class Application:
    def __init__(self, Application_name, category, company, app_size, no_of_users, ratings):
        self.Application_name = Application_name
        self.category = category
        self.company = company
        self.app_size = app_size
        self.no_of_users = no_of_users
        self.ratings = ratings

    def signup(self):
        print(f"Signup done, {self.Application_name}")

    def login(self):
        print(f"Welcome to application, {self.Application_name}")

    def logout(self):
        print("Successfully logged out")


    def show_details(self):
        print("----- Application Details -----")
        print(f"Name: {self.Application_name}")
        print(f"Category: {self.category}")
        print(f"Company: {self.company}")
        print(f"App Size: {self.app_size}")
        print(f"No. of Users: {self.no_of_users}")
        print(f"Ratings: {self.ratings}")
        print("--------------------------------")


app1 = Application("Instagram","Social Media","Meta","42.47 MB",1000,4.9)
app2 = Application("Facebook","Social Media","Meta","58.3 MB",2000,4.8)
app3 = Application("Snapchat","Social Media","Snap Inc.","25.1 MB",1500,4.5)
app4 = Application("PhonePe", "Finance", "PhonePe Pvt Ltd", "30.5 MB", 2500, 4.7)

app1.show_details()
app2.show_details()
app3.show_details()
app4.show_details()
