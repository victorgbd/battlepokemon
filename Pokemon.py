from random import randint
class Pokemon:
    #Constructor
    def __init__( self, level = 1, type = None ):
        self.__type  = [self.getRandomType(),type][type != None] 
        self.__level = level
        self.__hp    = self.__createHpByLevel()
        self.__hpMax = self.__hp
        self.__atk1  = self.__createAtks( self.__type )
        self.__atk2  = self.__createAtks( "normal" )
        self.__atk3  = self.__createAtks( "buff" )
        self.__atk4  = self.__createAtks( "buff" )
    
    # 1
    def getRandomType(self):
        types = ["agua","fuego","hierba"]
        return types[randint(0,2)]
        
    # 2 Metodo para crear un hp apropiado para el level
    def __createHpByLevel( self ):
        return randint( int( ( self.__level * 40 ) / 2 ), self.__level * 40 )
    
    # 3 Metodo para crear ataques por el tipo
    def __createAtks( self, type ):
        atk = {
                "type":type,
                "ap": None,
                "apMax": None,
                "dmg": randint( int( self.__level * 2.5 ), int(self.__level * 3.5) ) 
        }

        atk["ap"] = atk["apMax"] = randint( 15, 20 )

        if self.__level == 1 and type != "buff":
            atk["dmg"] = 20

        if type == "buff":
            buffType = ("proteccion","curacion")
            atk["type"] = buffType[randint(0,1)]
            atk["ap"] =  atk["apMax"] = randint( 2, 3 )
        
        if atk["type"] == "curacion":
            atk["dmg"] = self.__hpMax

        if atk["type"] == "proteccion":
            atk["dmg"] = None

        return atk


    #################################--Getter--#####################################
    # 4
    def getType(self):
        return self.__type
    # 5
    def getLevel(self):
        return self.__level
    # 6
    def getHp(self):
        return self.__hp
    # 7    
    def getHpMax(self):
        return self.__hpMax
    # 8    
    def getAtk1(self):
        return self.__atk1
    # 9    
    def getAtk2(self):
        return self.__atk2
    # 10    
    def getAtk3(self):
        return self.__atk3
    # 11
    def getAtk4(self):
        return self.__atk4
    ################################--End Getters--##################################

    #################################--Setter--#####################################
    # 12
    def setHp(self, hp):
        self.__hp = hp
    ################################--End Setters--##################################