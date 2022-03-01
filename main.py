from module import *

if __name__ == "__main__":
    dataset = Dataset("dataset1")
    #Genero N immagini cropped
    dataset.crop()
    #Filtro le N immagini cropped
    dataset.filter()
    #Applico delle rotazioni alle immagini filtrate
    dataset.rotate()
