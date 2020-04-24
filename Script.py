import keyboard
import time

#Delay for 3 seconds
time.sleep(3)

#Opens the text file
with open('Bee.txt','r') as file:


    for line in file:
    
    
        for word in line.split():
         
         
         keyboard.write(word)
         keyboard.send('enter')
         #Delay between each word sent
         time.sleep(0.3)