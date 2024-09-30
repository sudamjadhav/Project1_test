from users.models import *

# user1 = CustomUser.objects.get(id=3)
# print(dir(user1))
# print(user1.profile)

users_lst = CustomUser.objects.all()
print(users_lst)
# users_lst.delete()

# exec(open(r"D:\Study\Django\Projects\library2_0\db_shell.py").read())