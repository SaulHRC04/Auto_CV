
Auto_CV= "Programa esperado para la utilizacion de actualizacion de CV"
Nombre_Creador = "Realizado por Pre.Ing Saul Eduardo Hernadnez Rodriguez"
Fecha_UltimaActualizacion = "10/10/2024"
Licencia= "MIT"
PasosProg = "Instalacion Python"

def MensajeBienvenida():
    print(Auto_CV) 
    print (Nombre_Creador) 
    print (Fecha_UltimaActualizacion)
    print (Licencia) 
    print (PasosProg)

def PreguntasUsuario():
    
    Respuesta  = input ("Haz Realizado una certificacion en los ultimos dias?") 
    print(Respuesta)
    
    Respuesta1 = input ("Terminaste tu certificacion Si/No: ")
    if Respuesta1.lower() == "Si":
        print("Se puede agregar a tu CV!")
    else: 
        print("No se puede agregar a tu CV!")

PreguntasUsuario()