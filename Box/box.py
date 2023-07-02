# Personal date
userName = input('Enter your name: ')
userSurname = input("enter last name: ")
userMiddleName = input("Enter middle name:  ")

# Format
userName = userName.title()
userSurname = userSurname.title()
userMiddleName = userMiddleName.title()

# create data frame
personal_data = {
    "userName": userName,
    "userSurname": userSurname,
    "userMiddleName": userMiddleName,
    "pib": f"{userName} {userSurname} {userMiddleName}"
}
print(personal_data)
