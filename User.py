import uuid

class User:

    def __init__(self,name,password,username):
        self.__name = name
        self.__password = password
        self.__username = username
        self.__id = str(uuid.uuid4())[0:4]

    def __str__(self):
        return "id: {} Nombre: {} Contraseña: {} Usurario: {}".format(self.__id,
                                                                      self.__name,
                                                                      self.__password,
                                                                      self.__username)

    def get_id(self):
        return self.__id
    
    id = property(get_id)

from BDUser import *    
class UserMethod:
    """Clase para los método de Usuario
    Methods:
        add_user: @ClassMethod
        show_user: @classMethod
        search_user: @classMethod
        delete_user: @classMethod
    """
    @classmethod
    def add_user(cls):
        name = input("Ingrese el nombre de la persona: ")
        password = input("Ingrese la contraseña de la persona: ")
        username = input("Ingrese el nombre de usuario: ")
        user = User(name,password,username)
        return user
    
    @classmethod
    def show_users(cls,user_list):
        print("***************Lista de Usuarios Registrados**************")
        for user in user_list:
            print(user)
        print("**********************************************************")

    @classmethod
    def search_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user

    @classmethod
    def delete_user(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        return id_user


#user_list = bd_user()
#user = UserMethod.add_user()
#add_user_db(user,user_list)
#user = UserMethod.add_user()
#add_user_db(user,user_list)
#UserMethod.show_users(user_list)
#d_user = UserMethod.search_user()
#search_user_db(id_user, user_list)
#UserMethod.add_user()
#id_user = UserMethod.delete_user()
#delete_user_db(id_user,user_list)
#UserMethod.show_users(user_list)


#def wrapper_get_id(function):
 #   def hijo():
  #      print("******************************")
   #     id_user = input("Ingrese el id del usuario: ")
    #    function(id_user)
        
     #   print("******************************")
    #return hijo

#@wrapper_get_id
#def get_id(id_user):
 #   print(
  #      id_user)

#@wrapper_get_id
#def delete_user(id_user):
 #   print("Usuario eliminado")

#@wrapper_get_id
#def search_user(id_user):
 #   print("Usuario encontrado")


#delete_user()
#search_user()
#get_id()