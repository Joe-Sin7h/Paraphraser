from googletrans import Translator,LANGUAGES
from tkinter import *
import tkinter.scrolledtext as scrolledtext
import translate as ts
from textblob import TextBlob
from threading import Thread


#language codes in goolge trans >>> print(LANGUAGES)
'''{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian',
 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch',
  'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati'
  , 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 
  'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',
   'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian',
    'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian',
 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu',
  'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}'''


#--main--

root=Tk()  
root.iconbitmap('j.ico')                                #main window
#parapahsing function 
def tranlate_(): 

    try:
        global l5
        result_box.delete('1.0',END)
        d=TextBlob(text.get('1.0','end-1c'))  #getting the value in text widget 
        l=str(d.translate(to='fr'))
        d1=TextBlob(l)
        l2=str(d1.translate(to='en'))
        d2=TextBlob(l2)
        l2=str(d2.translate(to='ga'))
        d3=TextBlob(l2)
        l3=str(d3.translate(to='ru'))
        d4=TextBlob(l3)
        l4=str(d4.translate(to='sv'))
        d5=TextBlob(l4)
        l5=d5.translate(to='en')
        result_box.insert(END,l5)
                                                   #showing the result
    except TypeError as e:
        l.insert(END,'NOTHING IN THE INPUT BLOCK ABOVE !!!!!!'+"\n\n\n"+'OR CHECK YOUR INTERNET CONNECTION!!!!\n'+str(e))
    
# to save the input and output
def save_():
    try:
        f=open('output.txt','a+')

        f.write(str(l5)+'\n'+'-----------------------------------------------'*5+'\n')
        f.close()
        f1=open('input.txt','a+')
        f1.write(text.get('1.0','end-1c')+'\n'+'----------------------------------'*5+'\n')
        f1.close() 
    except:
        result_box.delete('1.0','end-1c')
        result_box.insert(END,'NOTHING TO SAVE ')  
#to clear the sreen (refresh)
def clear_():
    result_box.delete('1.0',END)
    text.delete('1.0',END)
root.geometry('1000x500')
root.wm_title('Paraphaser')
img_play=PhotoImage(file='Play-Button-PNG-HD.png')
img_exit=PhotoImage(file='Exit-PNG-Photos.png')
img_reload=PhotoImage(file='reload-icon-16900.png')
img_save=PhotoImage(file='Save-Button-PNG-Free-Image.png')
img_play=img_play.subsample(12,12)
img_exit=img_exit.subsample(6,5)
img_reload=img_reload.subsample(3,3)
img_save=img_save.subsample(20,20)
root.resizable(0,0)
main_frame=Frame(root)
main_frame.place(relwidth=1,relheight=1)
v=StringVar()
scrollbar = Scrollbar(main_frame)
scrollbar.place(x=900,y=0,relheight=0.5)
text = Text(main_frame, wrap=WORD, yscrollcommand=scrollbar.set)
text.place(relheight=0.5,relwidth=0.9)
text['font'] = ('consolas', '11')
scrollbar2 = Scrollbar(main_frame)
scrollbar2.place(x=900,y=250,relheight=0.5)
result_box=Text(main_frame,bg='white',yscrollcommand=scrollbar2.set,wrap=WORD)
result_box.place(x=2,y=250,relwidth=0.9,relheight=0.5)  
result_box['font'] = ('consolas', '11')
result_box.insert(END,'#'*10+' R E S U L T'+'#'*10)
scrollbar2.config(command=result_box.yview)
scrollbar.config(command=text.yview)
thread= Thread(target=tranlate_,)
# start button
button_start=Button(main_frame,text='start',command=thread.start,font=('Calibri',20),bg='white',activebackground='black',relief='flat',image=img_play)
button_start.place(relwidth=0.08,relheight=.25,x=918,y=0)
#save button
button_save=Button(main_frame,text='save',command=save_,font=('Calibri',20),bg='white',activebackground='black',relief='flat',image=img_save)
button_save.place(relwidth=0.08,relheight=.25,x=918,y=125)
#clear all(refresh) button
button_clear=Button(main_frame,text='clear',command=clear_,font=('Calibri',20),bg='white',activebackground='black',relief='flat',image=img_reload)
button_clear.place(relwidth=0.08,relheight=.25,x=918,y=250)
#exit button
button_exit=Button(main_frame,text='start',command=lambda:root.destroy(),font=('Calibri',20),bg='white',activebackground='black',relief='flat',image=img_exit)
button_exit.place(relwidth=0.08,relheight=.25,x=918,y=375)

root.mainloop()


