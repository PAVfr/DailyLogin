
import os
import locale


class Message:
    lang = "EN"

    def __init__(cls):
        if locale.getdefaultlocale()[0] == 'fr_FR':
            Message.lang = "FR"
        else:
            Message.lang = "EN"

    @classmethod
    def user_logged(cls):
        if cls.lang == "FR":
            return "\tUtilisateur : \t"
        else:
            return "\tUser : \t"

    @classmethod
    def dosid(cls):
        if cls.lang == "FR":
            return "\tdosid : \t"
        else:
            return "\tdosid : "

    @classmethod
    def client(cls):
        if cls.lang == "FR":
            print("\n\tLe client par défaut est utilisé.\n")
        else:
            print("\n\tThe default client is used.\n")

    @classmethod
    def task_update(cls):
        if cls.lang == "FR":
            print("\n\tLa tâche a bien été ajoutée/modifié.\n\n")
        else:
            print("\n\tThe task has been added/modified.\n\n")

    @classmethod
    def last_version(cls):
        if cls.lang == "FR":
            print(f"\n\tVous n'avez pas la dernière version. Merci de la télécharger.\n\n")
        else:
            print(f"\n\tYou don't have the latest version. Thanx you to download it.\n\n")

    @classmethod
    def file_account(cls):
        if cls.lang == "FR":
            return "\n".join([
                "# Une ligne par compte.",
                "# Séparer l'utilisateur et le mot de passe par : Espace ou Tabulation",
                "#",
                "# Exemple :",
                "# myuser 123456789",
                "#",
                "# |",
                "# V"
                "\n"])
        else:
            return "\n".join([
                "# One line per account.",
                "# Separate user and password by: Space or Tab",
                "#",
                "# Example :",
                "# myuser 123456789",
                "#",
                "# |",
                "# V"
                "\n"])


    @classmethod
    def user_pass_error(cls):
        if cls.lang == "FR":
            print("\tLe nom utilisateur et/ou le mot de passe sont incorrects\n")
        else:
            print("\tIncorrect user name and/or password\n")




    # Calendar

    @classmethod
    def calendar_already_done(cls, user):
        if cls.lang == "FR":
            print(f"\tLa connexion du compte {user} a déjà été faite.\n")
        else:
            print(f"\tThe account {user} has already been logged in.\n")

    @classmethod
    def calendar_no_rewards_left(cls, user):
        if cls.lang == "FR":
            print(f"\tToutes les récompenses de {user} ont été faites.\n")
        else:
            print(f"\tNo rewards left for the account : {user}\n")

    @classmethod
    def calendar_done(cls, user):
        """
        :param user: Utilisateur
        """
        if cls.lang == "FR":
            print(f"\tLa connexion a bien été faite sur le compte : {user}\n")
        else:
            print(f"\tThe connection has been made on the account: {user}\n")

