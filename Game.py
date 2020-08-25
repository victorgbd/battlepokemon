from Pokemon import Pokemon
from AI import AI
from random import randint
import os
import sys

class Game:
    def __init__(self):
        self.__Ai           = AI()
        self.__pk_IA        = None
        self.__pk_User      = None
        self.__rangoLevel   = [25,30]
        self.__efectividad  = randint(1,10)
        self.__traduccion   = {
            "nothing"   :0,
            "fuego"     :1,
            "agua"      :2,
            "hierba"    :3,
            "normal"    :4,
            "proteccion":5,
            "curacion"  :6,
            
        }
        self.__traduccion_reverse = {
            0   :"nothing",
            1   :"fuego",
            2   :"agua",
            3   :"hierba",
            4   :"normal",
            5   :"proteccion",
            6   :"curacion" 
        }
        
    # 1
    def start(self):
        print("Cargando...")
        self.__clear()
        self.__setConfig()
        
        #Bucle de la batalla
        turno = randint(1,2)

        while self.__getHpFromPokemons():
            if turno == 1:
                turno = 2
                self.__playerOptions()
            else:
                turno = 1
                self.__iAOptions()

        #Autoentrenar
        try:
            self.__Ai.learn()
        except Exception as e:
            print(e)

        print("###############[Fin del juego]###############")

        if  self.__pk_IA.getHp() > self.__pk_User.getHp():          
            print("[Ganador: ---- IA ----]")
        else:
            print("[Ganador: ---- Jugador ----]")
              
    # 2
    def __playerOptions( self ):
        decision = None
        while True:
            input()
            self.__clear()
            print("##########[PLAYER]##################")
            print("####[ PK: {}".format( self.__pk_User.getType().capitalize() ))
            print("####[ LEVEL: {}".format( self.__pk_User.getLevel() ))
            print("####[ HP: {}".format( self.__hpToBar(self.__pk_User.getHp(), self.__pk_User.getHpMax())  ))
            #print(self.__pk_User.getHp())
            print("##########[IA]######################")
            print("####[ PK: {}".format( self.__pk_IA.getType().capitalize() ))
            print("####[ LEVEL: {}".format( self.__pk_IA.getLevel() ))
            print("####[ HP: {}".format( self.__hpToBar( self.__pk_IA.getHp(), self.__pk_IA.getHpMax()) ))
            print("####################################")
            #print(self.__pk_IA.getHp())
            while True:
                print("\n###############[Seleccione un ataque]###############")
                print("1: {} [dmg:{}] (ap:{}/{})".format(self.__pk_User.getAtk1()["type"].capitalize(),self.__pk_User.getAtk1()["dmg"],self.__pk_User.getAtk1()["ap"],self.__pk_User.getAtk1()["apMax"]))
                print("2: {} [dmg:{}] (ap:{}/{})".format(self.__pk_User.getAtk2()["type"].capitalize(),self.__pk_User.getAtk2()["dmg"],self.__pk_User.getAtk2()["ap"],self.__pk_User.getAtk2()["apMax"]))
                print("3: {} [dmg:{}] (ap:{}/{})".format(self.__pk_User.getAtk3()["type"].capitalize(),self.__pk_User.getAtk3()["dmg"],self.__pk_User.getAtk3()["ap"],self.__pk_User.getAtk3()["apMax"]))
                print("4: {} [dmg:{}] (ap:{}/{})".format(self.__pk_User.getAtk4()["type"].capitalize(),self.__pk_User.getAtk4()["dmg"],self.__pk_User.getAtk4()["ap"],self.__pk_User.getAtk4()["apMax"]))
                print("5: -> Escapar")
                try:
                    optAtk = int(input()) 
                    ##POR REVISAR, SE PUEDE SIMPLIFICAR
                    if optAtk > 0 and optAtk < 6:
                        if optAtk==1:
                            if self.__pk_User.getAtk1()["ap"] > 0:
                                if self.__efectividad != 1:
                                    self.__hpsubtract(self.__pk_User.getAtk1()["type"],self.__pk_User.getAtk1()["dmg"],self.__pk_User,self.__pk_IA)
                                    self.__apsubtract(self.__pk_User.getAtk1()["type"],self.__pk_User)
                                else:
                                    self.__efectividad= randint(1,10)
                                    self.__apsubtract(self.__pk_User.getAtk1()["type"],self.__pk_User)
                                decision = self.__pk_User.getAtk1()["type"]
                                break
                            else:
                                print("ya no puedes usar esta opcion")    
                        elif optAtk==2:
                            if self.__pk_User.getAtk2()["ap"] > 0:
                                if self.__efectividad != 1:
                                    self.__hpsubtract(self.__pk_User.getAtk2()["type"],self.__pk_User.getAtk2()["dmg"],self.__pk_User,self.__pk_IA)
                                    self.__apsubtract(self.__pk_User.getAtk2()["type"],self.__pk_User)
                                else:
                                    self.__efectividad= randint(1,10)
                                    self.__apsubtract(self.__pk_User.getAtk2()["type"],self.__pk_User)
                                decision = self.__pk_User.getAtk2()["type"]
                                break
                            else:
                                print("ya no puedes usar esta opcion")     
                        elif optAtk==3:
                            if self.__pk_User.getAtk3()["ap"] > 0:
                                if self.__efectividad != 1:
                                    self.__hpsubtract(self.__pk_User.getAtk3()["type"],self.__pk_User.getAtk3()["dmg"],self.__pk_User,self.__pk_IA)
                                    self.__apsubtract(self.__pk_User.getAtk3()["type"],self.__pk_User)
                                else:
                                    self.__efectividad= randint(1,10)
                                    self.__apsubtract(self.__pk_User.getAtk3()["type"],self.__pk_User)
                                decision = self.__pk_User.getAtk3()["type"]
                                break
                            else:
                                print("ya no puedes usar esta opcion")     
                        elif optAtk == 4:
                            if self.__pk_User.getAtk4()["ap"] > 0:
                                if self.__efectividad != 1:
                                    self.__hpsubtract(self.__pk_User.getAtk4()["type"],self.__pk_User.getAtk4()["dmg"],self.__pk_User,self.__pk_IA)
                                    self.__apsubtract(self.__pk_User.getAtk4()["type"],self.__pk_User)
                                else:
                                    self.__efectividad= randint(1,10)
                                    self.__apsubtract(self.__pk_User.getAtk4()["type"],self.__pk_User)
                                decision = self.__pk_User.getAtk4()["type"]
                                break
                            else:
                                print("ya no puedes usar esta opcion")  
                        elif optAtk == 5:
                            
                            sys.exit(0)                                                              
                    else:
                        print("Seleciones una opción válida")
                except Exception as e:
                    print(e)
            
            try:
                atk1 = self.__traduccion[ self.__pk_User.getAtk1()['type'] ]
                atk2 = self.__traduccion[ self.__pk_User.getAtk2()['type'] ]
                atk3 = self.__traduccion[ self.__pk_User.getAtk3()['type'] ]
                atk4 = self.__traduccion[ self.__pk_User.getAtk4()['type'] ]

                result = [
                    self.__traduccion[ self.__pk_IA.getType() ],
                    self.__traduccion[ self.__pk_User.getType() ],
                    atk1,
                    atk2,
                    atk3,
                    atk4,
                    int( ( self.__pk_IA.getHp() / self.__pk_IA.getHpMax() ) * 100 ), #LO LLEVA A PORCIENTO
                    int( ( self.__pk_User.getHp() / self.__pk_User.getHpMax() ) * 100 ),
                    decision
                ]

                self.__Ai.memorize( result )
            except Exception as e:
                print(e)
            
            break
                 
        
    # 3         
    def __iAOptions(self):
        #print("1: {} [dmg:{}] (ap:{}/{})".format(self.__pk_IA.getAtk1()["type"].capitalize(),self.__pk_IA.getAtk1()["dmg"],self.__pk_IA.getAtk1()["ap"],self.__pk_IA.getAtk1()["apMax"]))
        #print("2: {} [dmg:{}] (ap:{}/{})".format(self.__pk_IA.getAtk2()["type"].capitalize(),self.__pk_IA.getAtk2()["dmg"],self.__pk_IA.getAtk2()["ap"],self.__pk_IA.getAtk2()["apMax"]))
        #print("3: {} [dmg:{}] (ap:{}/{})".format(self.__pk_IA.getAtk3()["type"].capitalize(),self.__pk_IA.getAtk3()["dmg"],self.__pk_IA.getAtk3()["ap"],self.__pk_IA.getAtk3()["apMax"]))
        #print("4: {} [dmg:{}] (ap:{}/{})".format(self.__pk_IA.getAtk4()["type"].capitalize(),self.__pk_IA.getAtk4()["dmg"],self.__pk_IA.getAtk4()["ap"],self.__pk_IA.getAtk4()["apMax"]))
                
        atk1 = self.__traduccion[ self.__pk_IA.getAtk1()['type'] ]
        atk2 = self.__traduccion[ self.__pk_IA.getAtk2()['type'] ]
        atk3 = self.__traduccion[ self.__pk_IA.getAtk3()['type'] ]
        atk4 = self.__traduccion[ self.__pk_IA.getAtk4()['type'] ]
        
        if self.__pk_IA.getAtk1()["ap"] == 0:
            atk1 = 0
        if self.__pk_IA.getAtk2()["ap"] == 0:
            atk2 = 0
        if self.__pk_IA.getAtk3()["ap"] == 0:
            atk3 = 0
        if self.__pk_IA.getAtk4()["ap"] == 0:
            atk4 = 0
        
        datosToIA = [   self.__traduccion[ self.__pk_IA.getType() ],
                        self.__traduccion[ self.__pk_User.getType() ],
                        atk1,
                        atk2,
                        atk3,
                        atk4,
                        int( ( self.__pk_IA.getHp() / self.__pk_IA.getHpMax() ) * 100 ), #LO LLEVA A PORCIENTO
                        int( ( self.__pk_User.getHp() / self.__pk_User.getHpMax() ) * 100 )
                    ]

        #obtencion del resultado de la IA
        predict = self.__Ai.predict( datosToIA )

        #print(datosToIA)
        #print(predict)

        print("####################################################")
        print("###[ IA usó: {} {}]".format(predict, ["pero falló",""][self.__efectividad != 1]))
        print("####################################################")

        dmg = 0

        if self.__pk_IA.getAtk1()["type"] == predict:
            dmg = self.__pk_IA.getAtk1()["dmg"]
        elif self.__pk_IA.getAtk2()["type"] == predict:
            dmg = self.__pk_IA.getAtk2()["dmg"]
        elif self.__pk_IA.getAtk3()["type"] == predict:
            dmg = self.__pk_IA.getAtk3()["dmg"]
        elif self.__pk_IA.getAtk4()["type"] == predict:
            dmg = self.__pk_IA.getAtk4()["dmg"]  
        
        if self.__efectividad != 1:
            self.__hpsubtract( predict, dmg, self.__pk_IA, self.__pk_User )
            self.__apsubtract( predict, self.__pk_IA )
        else:
            self.__apsubtract( predict, self.__pk_IA )
            self.__efectividad = randint(1,10)

    
    # 4
    def __setConfig(self):
        #Obtencion de datos
        print("###############[Selecciona un tipo de pokemon]###############")
        print("|## [1] => [Fuego]\n|## [2] => [Agua]\n|## [3] => [Hierba]")
        print(">>")
        pk_user_type = int( input() )
        while True:
            try:
                self.__clear()
                print("###############[Selecciona un rango de niveles válidos que tendrán los pokemones]###############")
                print("Desde el nivel:")
                self.__rangoLevel[0] = int(input())
                print("Hasta el nivel:")
                self.__rangoLevel[1] = int(input())
                if self.__rangoLevel[0] < self.__rangoLevel[1]: 
                    break
            except:
                pass

        #Configurar despues de obter los datos
        self.__pk_User  = Pokemon( randint( self.__rangoLevel[0], self.__rangoLevel[1]), self.__traduccion_reverse[pk_user_type] )
        self.__pk_IA    = Pokemon( randint( self.__rangoLevel[0], self.__rangoLevel[1]) )
    # 5
    def __getHpFromPokemons(self):
        return self.__pk_IA.getHp() > 0 and self.__pk_User.getHp() > 0
    # 6
    def __clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return None
    # 7
    #restara o sumara el hp de los jugadores
    def __hpsubtract( self, atk, dmg, op1, op2 ):
        if atk in ['agua','fuego','hierba','normal']:
            if op1.getType() ==  'fuego' and op2.getType() ==  'hierba':
                op2.setHp( op2.getHp() - (dmg * 2) )
            elif op1.getType() ==  'agua' and op2.getType() ==  'fuego':
                op2.setHp( op2.getHp() - (dmg * 2) )
            elif op1.getType() ==  'hierba' and op2.getType() ==  'agua':
                op2.setHp( op2.getHp() - (dmg * 2) )
            elif op1.getType() ==  op2.getType():
                op2.setHp( op2.getHp() - (dmg * 0.5) )
            else:
                op2.setHp( op2.getHp() - dmg )
        elif atk =='curacion':
            op1.setHp( dmg )
        elif atk =='proteccion':
            self.__efectividad = 1
    # 8        
    def __apsubtract( self, atk, op ):        
        if op.getAtk1()['type'] == atk and op.getAtk1()["ap"] != 0:
            op.getAtk1()["ap"] = op.getAtk1()["ap"]-1
        elif op.getAtk2()['type'] == atk and op.getAtk2()["ap"] != 0:
            op.getAtk2()["ap"] = op.getAtk2()["ap"]-1
        elif op.getAtk3()['type'] == atk and op.getAtk3()["ap"] != 0:
            op.getAtk3()["ap"] = op.getAtk3()["ap"]-1
        elif op.getAtk4()['type'] == atk and op.getAtk4()["ap"] != 0:
            op.getAtk4()["ap"] = op.getAtk4()["ap"]-1
    # 9 
    def __hpToBar( self, hp, hpMax ):
        bars = 15
        hpToPorcent = ( hp / hpMax ) * bars
        bar = "["
        for i in range( int( hpToPorcent ) ):
            bar += "#"
        barLeft = bars - len(bar)
        for i in range( barLeft ):
            bar += " "
        bar += "]"
        return bar

