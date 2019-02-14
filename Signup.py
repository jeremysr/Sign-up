#ver1.2
class Ticket: #class is an object that holds infomation
    
    _ids = count(0)
    
    def __init__(self, image, name, email, date_of_birth, check_in):
        self.id = next(self.ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in


#test data
Ticket = [
    Ticket("Jeremy","hmjzone@gmail.com","20.02.2002",False),
    Ticket("Jerry","jerry@gmail.com","14.06.2003",False),
    Ticket("Moses","moses@gmail.com","01.04.2001",False),
    Ticket("Dom","dom@gmail.com","15.03.2002",False)
    ]



#pages
#index page
@route("/")
@view("index")
def index():
    pass

run(host='0.0.0.0', port = 8080, reloader = True, debug = True)
