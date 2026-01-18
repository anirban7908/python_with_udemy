def format_name(f_name, l_name):
    formatted_name = (f_name +' '+ l_name).title()
    return  formatted_name

fullname = format_name('anirban', 'choudhury')
print(fullname)