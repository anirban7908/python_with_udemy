def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please provide all details first name and last name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input('Enter First name: '), input('Enter Last name: ')))
