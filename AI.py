import random
from Data import Answers
from Data import temp_user_data
from Data import conversation
from Data import change_user_data

keys_tuple_list=list()
keys_lists_list=list()
values_lists_list=list()

for a in Answers.keys():
    keys_tuple_list.append(a)

for b in keys_tuple_list:
    keys_lists_list.append(list(b))

for c in Answers.values():
    values_lists_list.append(c)

#Counter for responses given till now used to initiate conversation
response_count = 0

def Answer(query):

    global response_count
    percentage_dict = {}
    
    #loop for list of lists ("Hii", Hello)
    for k in keys_lists_list:
        query_list=list(query)

        #loop for element in list "Hii'
        for e in k:
            char_list=list(e)
            score = 0.0
            
            #Letters matches
            points1 = 0
            #letters not matched
            points2 = 0
            position_counter1 = 0
            #Main loop for checking elements
            for i in query_list:
                position_counter2 = 0
                position_counter1 = position_counter1 + 1
                for v in char_list:

                    position_counter2 = position_counter2 + 1
                    if position_counter1 == position_counter2:
                        if i.lower() == v.lower():
                            points1 += 1
                            break
                        elif i.lower() != v.lower():
                            points2 += 1
                            break
                        else:
                            pass
            score = ((points1 - points2) / len(query_list)) * 100
            percentage_dict[e] = score
    
    try:
        main_val_key_half = max(percentage_dict, key=percentage_dict.get)
        if percentage_dict[main_val_key_half] < 0:
            raise ValueError
        for key in Answers:
            for words in key:
                if words.lower() == main_val_key_half.lower():
                    response_count += 1
                    return random.choice(Answers[key])
    except:
        not_found = "?"
        response_count += 1
        return not_found

#Data for Store
temp_data_ask_store = ""

def Ask():
    global temp_data_ask_store
    unfilled = []
    for info in temp_user_data:
        if temp_user_data[info] == "":
            unfilled.append(info)
    
    print(unfilled) #Remove this

    question_dat = random.choice(unfilled)
    temp_data_ask_store = question_dat
    index = -1
    for i in temp_user_data:
        index += 1
        if temp_user_data[i] == temp_user_data[question_dat]:
            return conversation[index]

def Store(query):
    global response_count
    key = temp_data_ask_store
    change_user_data(key, query)
    return "Nice"

import tkinter
from tkinter import Entry, ttk
from tkinter import scrolledtext
from PIL import Image

flag = False
def write():
    global flag
    global response_count
    if flag == True:
        Query=input_area.get().title()
        text_area.config(state='normal')
        text_area.insert('end',"You: "+Query+"\n")
        text_area.insert('end',"RumI: "+Store(Query)+"\n")
        text_area.config(state='normal')
        input_area.delete(0,'end')
        response_count = 0
        flag = False
    else:
        Query=input_area.get().title()
        text_area.config(state='normal')
        text_area.insert('end',"You: "+Query+"\n")
        text_area.insert('end',"RumI: "+Answer(Query)+"\n")
        text_area.config(state='normal')
        input_area.delete(0,'end')

    if response_count == 2:
        text_area.insert('end',"RumI: "+Ask()+"\n")
        flag = True

win = tkinter.Tk()
win.maxsize(350,600)
win.minsize(350,600)
win.configure(bg="lightgray")

chat_label = tkinter.Label(win,text="Chat", bg="lightgray")
chat_label.config(font=("Arial",12))
chat_label.pack(padx=20, pady=5)

text_area = tkinter.scrolledtext.ScrolledText(win)
text_area.pack(padx=20, pady=5)
text_area.insert('end',"RumI: Hello\n")
text_area.config(state='disabled')

msg_label = tkinter.Label(win,text="Message", bg="lightgray")
msg_label.config(font=("Arial",12))
msg_label.pack(padx=20, pady=5)

input_area = Entry(win,width=100)
input_area.pack(padx=20,pady=5)
input_area.bind("<Return>",write)
input_area.focus_set()

send_button = tkinter.Button(win, text="Send",command=write)
send_button.config(font=("Arial",12))
send_button.pack(padx=20,pady=5)

win.mainloop()  