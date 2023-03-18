import os 
import tkinter as tk1 
import datetime as dt1 
import pyautogui as pag1 
import cv2 
import requests
clear = lambda: os.system('cls')
clear()
def set_area1(): 
    a1 = frame2.geometry().strip().replace( "x", " " ).replace( "+", " " ).split( " " ) 
    a2 = [0,0,0,0] 
    a2[0] = str( int( a1[2] ) +10 )
    a2[1] = str( int( a1[3] ) +38 )
    a2[2] = str( int( a1[0] )  -2 ) 
    a2[3] = str( int( a1[1] )  -2 ) 
    str2 = " ".join( a2 ) 
    textbox1.delete( 0, tk1.END ) 
    textbox1.insert( 0, str2 ) 
    frame2.attributes( "-alpha", 1.0 ) 
    frame2.attributes( "-transparentcolor", "white" ) 
    str3 = dt1.datetime.now().strftime( "%Y%m%d_%H%M%S" ) + ".png" 
    textbox2.delete( 0, tk1.END ) 
    textbox2.insert( 0, str3 ) 

def click1(): 
    set_area1() 
    a1 = textbox1.get().strip().split( " " ) 
    img1 = pag1.screenshot( region=(int(a1[0]), int(a1[1]), int(a1[2]), int(a1[3])) )  # x, y, w, h 
    path1 = os.path.dirname(__file__) + "\\" 
    file1 = path1 + textbox2.get().strip() 
    img1.save( file1 )
    URL="https://upload.gyazo.com/api/upload"
    headers = {'Authorization': "Bearer {}".format('Gyazo API KEY')}
    with open(file1,"rb") as f:
        files = {'imagedata':f.read()}
        response = requests.request('post', URL, headers=headers, files=files)
        asdfsghf=response.text[response.text.find('"url":"'):response.text.find('","access_policy":null}')]
        print(asdfsghf.replace('"url":"',''))
    return 1 

frame1 = tk1.Tk()
frame1.title("Gyazo Uploader")
frame1.geometry('350x70+1000+100')
frame1.grid()

btn1 = tk1.Button(frame1, text='capture', command=click1, bg='#F9A0A0')
btn1.place(x=220, y=20, width=120)

textbox1 = tk1.Entry(master=frame1)
textbox1.place(x=20, y=100, width=200) 
textbox1.insert(0, "")

textbox2 = tk1.Entry(master=frame1)
textbox2.place(x=20, y=20, width=180) 
textbox2.insert(0, "") 

frame2 = tk1.Toplevel()

frame2.title("area")
frame2.geometry('800x500+100+100')
frame2.attributes("-alpha", 0.5 ) 
frame2.config(bg="white") 

frame2.grid()
frame2.lift() 

frame1.mainloop()
