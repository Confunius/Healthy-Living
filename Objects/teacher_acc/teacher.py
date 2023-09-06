class Teacher:
    count_id = 0
    def __init__(self,userFullName,userName,userPassword,userEmail, userCfmPassword, userAddress, userPostalCode, userVerified=0): # initializer method    def __init__(self, userName, userPassword, userEmail, userCfmEmail):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__userFullName = userFullName
        self.__userName = userName
        self.__userPassword = userPassword
        self.__userEmail = userEmail
        self.__userCfmPassword = userCfmPassword
        self.__userAddress = userAddress
        self.__userPostalCode = userPostalCode
        self.__userVerified = userVerified

    def __repr__(self):
        return f'<User: {self.__userName}>'    # accessor methods

    def get_user_id(self):
        return self.__user_id

    def get_userName(self):
        return self.__userName

    def get_userPassword(self):
        return self.__userPassword

    def get_userEmail(self):
        return self.__userEmail

    def get_userCfmPassword(self):
        return self.__userCfmPassword

    def get_userAddress(self):
        return self.__userAddress

    def get_userPostalCode(self):
        return self.__userPostalCode

    def get_userVerified(self):
        return self.__userVerified

    def get_userFullName(self):
        return self.__userFullName

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_userName(self, userName):
        self.__userName = userName

    def set_userPassword(self, userPassword):
        self.__userPassword = userPassword

    def set_userEmail(self, userEmail):
        self.__userEmail = userEmail

    def set_userCfmPassword(self, userCfmPassword):
        self.__userCfmPassword = userCfmPassword

    def set_userAddress(self, userAddress):
        self.__userAddress = userAddress

    def set_userPostalCode(self, userPostalCode):
        self.__userPostalCode = userPostalCode

    def set_userVerified(self, userVerified):
        self.__userVerified = userVerified

    def set_userFullName(self, userFullName):
        self.__userFullName = userFullName
