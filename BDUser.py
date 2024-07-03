def bd_user():
    return []

def add_user_db(user,user_list):
    user_list.append(user)
    print("Usuario Agregado")
    
def search_user_db(id_user,user_list):
    print("*************Busqueda de Usuario***********")
    for index,user in enumerate(user_list):
        if id_user == user.id:
            print(user_list[index])
            break
        else:
            print("Usuario no Encontrado")
    print("******************************************")    

def delete_user_db(id_user,user_list):
    print("*************Borrado de Usuario***********")
    for index,user in enumerate(user_list):
        if id_user == user.id:
            user_list.pop(index)
            break
        #else:
         #    print("Usuario no Encontrado")
    print("******************************************")