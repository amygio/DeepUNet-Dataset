
import numpy as np
import cv2
import os, glob
import random
class Dataset:

    def __init__(self,path):
        self.path=path

    
    def crop(self):
        img_path=self.path + "/img"
        label_path=self.path + "/label"        

        for file_name in os.listdir(img_path):

            image = cv2.imread(os.path.join(img_path, file_name))
            label = cv2.imread(os.path.join(label_path, file_name))
            shape = image.shape
            height = shape[0]
            width = shape[1]
            #Seleziono in maniera random dei punti in un certo range calcolato in modo tale che si possa fare il crop senza rischiare di uscire dall'immagine 
            for i in range (0,3):
                x = random.randrange(0, width - 256)
                y = random.randrange(0, height - 256)
                # crop size 256x256
                cropped_img = image[y:y+256, x:x+256]
                cropped_label = label[y:y+256, x:x+256]
                cv2.imwrite(os.path.join(self.path + "/cropped_img",str(i)+file_name), cropped_img)
                cv2.imwrite(os.path.join(self.path + "/cropped_label",str(i)+file_name), cropped_label)
        
    def filter(self):
        img_path=self.path + "/cropped_img"
        label_path=self.path + "/cropped_label"

        for file_name in os.listdir(label_path):
            count=0
            image = cv2.imread(os.path.join(img_path,file_name))
            label = cv2.imread(os.path.join(label_path,file_name),0)
            cols, rows = label.shape
            for y in range(cols):
                for x in range(rows):
                    if(label[y,x]==255):
                        #conto il numero di pixel di mare
                        count += 1
            #calcolo la percentuale di pixel di mare
            perc=(count/(rows*cols))*100
            #se questa percentuale è compresa tra 20% e 60% allora ritengo l'immagine valida altrimenti significa che c'è poco mare o poca terra
            if(perc>=15 and perc<=70):
                cv2.imwrite(os.path.join(self.path + "/filtered_img",file_name), image)
                cv2.imwrite(os.path.join(self.path + "/filtered_label",file_name), label)




                    

            






    








        



