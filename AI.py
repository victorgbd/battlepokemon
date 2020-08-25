from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 
from pandas import DataFrame
from Database import Database

class AI:
    def __init__(self):
        # INSTANCIA DE LA BASE DE DATOS
        self.__db = Database()
        # MEMORIA DEL ALGORITMO
        self.__memory = []

        __data = DataFrame( self.__db.getDatas() )
        __data.columns = ["op1","op2","atk1","atk2","atk3","atk4","hp1","hp2","result"]

        __x = __data.drop( 'result', axis = 1 ).values
        __y = __data['result'].values
        
        self.__x_train,self.__x_test,self.__y_train,self.__y_test = train_test_split( __x, __y, test_size = 0.2, random_state = 3, stratify = __y )
        
        self.__tree = RandomForestClassifier(n_estimators = 17, criterion = "entropy", max_depth = 13, min_samples_split = 2, random_state = 99)
        self.__tree.fit( self.__x_train, self.__y_train )

    # 1 Método para obtener el score de el algorimo ::RETORNA UN STRING::
    def score( self ):
        return str(int((self.__tree.score(self.__x_test,self.__y_test)) * 100)) + "%"

    # 2 Método para predecir el siguiente ataque ::RETORNA UN STRING::
    def predict( self, info ):  
        pred = self.__tree.predict( [ info ] )
        return pred[0]

    # 3 Método para guardar las batallas de la lista temporal en la base de datos
    def learn(self):
        self.__db.insertDatas( self.__memory )

    # 4 Método para guardar las batallas en una lista temporal
    def memorize( self, info ):
        self.__memory.append( info )

    def getMemory(self):
        return self.__memory