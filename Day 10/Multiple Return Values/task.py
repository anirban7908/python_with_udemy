def format_name(f_name, l_name):
<<<<<<< HEAD
=======
    if f_name == "" or l_name == "":
        return "Please provide all details first name and last name"
>>>>>>> origin/master
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


<<<<<<< HEAD
print(format_name("AnGEla", "YU"))
=======
print(format_name(input('Enter First name: '), input('Enter Last name: ')))
>>>>>>> origin/master
