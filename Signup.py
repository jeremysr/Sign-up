from bottle import run, route, view, get, post, request
from itertools import count

#ver 1.3

class Ticket: #class is an object that holds infomation

    _ids = count(0)

    def __init__(self,name, email, date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in


#test data
tickets = [
    Ticket("Jeremy","hmjzone@gmail.com","20/02/2002",False),
    Ticket("Tom","tom@gmail.com","14/06/2003",False),
    Ticket("Moses","moses@gmail.com","01/04/2001",False),
    Ticket("Dom","dom@gmail.com","15/03/2002",False)
]



#pages
#index page
@route('/')
@view('index')
def index():
    pass

#pages
#check-in page
@route('/check-in')
@view('check-in')
def check_in():
    data = dict (ticket_list = tickets)
    return data

#pages
#sell ticket page
@route('/sell-ticket')
@view('sell-ticket')
def sell_ticket():
    pass


@route('/sell-ticket-success', method ="POST")
@view('sell-ticket-success')
def sell_ticket_success():
    name = request.forms.get('name')
    email = request.forms.get('email')
    date_of_birth = request.forms.get('dob')
    
    new_ticket = Ticket(name, email, date_of_birth, False)
    tickets.append(new_ticket)
    



'''
this changes a ticket status to "check in" and
displays the result to the user
'''
@route('/check-in-success/<ticket_id>')
@view ('check-in-success')
def check_in_success(ticket_id):
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
    data = dict (ticket = found_ticket)
    found_ticket.check_in = True
    return data

run(host='0.0.0.0', port = 8080, reloader = True, debug = True)
