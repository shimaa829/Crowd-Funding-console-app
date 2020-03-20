import re
import json

def registartion(user_id):

    user_id += 1

    first_name = input("First name : ")
    last_name = input("Last name : ")
    email = input("Email : ")
    password = input("Password : ")
    confirm_password = input("Confirm password : ")
    mobile_phone = input("Mobile phone : ")

    list_data = {'user_id': user_id,'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password,
                 'mobile_phone': mobile_phone}

    if password == confirm_password:
        if re.match("^01[0125][0-9]{8}$", mobile_phone):
            users_data = open("users_data.json", "a")
            json.dump(list_data, users_data)
            users_data.write("\n")
            users_data.close()

    else:
        print("\nYour data is invalid ,, please enter valid data :")
        registartion(user_id)