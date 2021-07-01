import random
from Data import Answers
from Data import conversation

temp_user_data={

    "Favorite color":"",
    "Favorite food":"",
    "Favorite singer":"",
    "Favorite acter/actress":"",
    "Favorite song":"",
    "Gender":"",
    "Relationship status":"",
    "Social media":"",
    "Possible_Interests": ["Computers", "Singing", "Dancing", "Coding/Programming", "Studying", "Physics", "Chemistry", "Maths", "Biology", "Acting", "Streaming", "Music", "Movies", "Binge_watching", "Gaming", "Reading"],
    "Interests": []
}

keys_tuple_list=list()
keys_lists_list=list()
values_lists_list=list()
flag = False
#Counter for responses given till now used to initiate conversation
response_count = 0

for a in Answers.keys():
    keys_tuple_list.append(a)

for b in keys_tuple_list:
    keys_lists_list.append(list(b))

for c in Answers.values():
    values_lists_list.append(c)


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

dump = ""
def Ask():
    global dump
    unfilled = []
    for info in temp_user_data.keys:
        if temp_user_data[info] == "":
            unfilled.append(info)

    question_dat = random.choice(unfilled)
    dump = quesion_dat
    index = -1
    for i in temp_user_data:
        index += 1
        if temp_user_data[i] == temp_user_data[question_dat]: 
		return conversation[index]
def Store(query):
    global dump
    temp_user_data[dump] = query
	

while True:
	user_query = input()
	printf("You : {user_query}")
	ans = Answer(user_query)
	if response_count == 2:
		print(ans)
		Ask()
		query = input(":")
		Store()
	else:
		print(ans)
