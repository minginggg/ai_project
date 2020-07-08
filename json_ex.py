import json
import getpass




def read_json():
    with open('students.json','r',encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    return json_data

def write_json(json_data):
    with open('students.json','w',encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False)


def all_name(json_data):
        print("모든 학생의 이름")
        for i in range(len(json_data["student"])):
            print(json_data["student"][i]["name"])
        


def minor(json_data):
    print("미성년자")
    for i in range(len(json_data["student"])):
        if int(json_data["student"][i]["age"]) < 20:
            print("이름:" ,json_data["student"][i]["name"], ", 나이:",json_data["student"][i]["age"])

def minor_write(json_data):
    user = {}
    user['name'] = input("이름:")
    user['age'] = input("나이:")
    user['job'] = input("직업:")
    user['user_id'] = input("아이디:")
    user['password'] = getpass.getpass("비밀번호")
   
    # with open('students.json','r',encoding='utf-8') as feedsjson:
    #     json_data = json.load(feedsjson)
    json_data['student'].append(user)
    write_json(json_data)
    
Users = read_json()
all_name(Users)
minor_write(Users)
minor(Users)





# json_data['student'] = {"name":"켱", "age":"15","job":"student","user_id":"hello","password":"1515"}
# print(json.dump(json_data) )