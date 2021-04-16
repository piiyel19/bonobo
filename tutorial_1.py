import bonobo
import requests

def extract():

    #extract data json
    books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
    ]
    
    #sorting your data in list
    collect = []
    for xdata in books:   
        xid = xdata["id"]
        title = xdata["title"]
        author = xdata["author"]
        
        collect.append(xid)
        collect.append(title)
        collect.append(author)

        yield collect
        collect = []
        

def transform(s):
    d = s
    length = len(d)
    #print("#######")
    for i in range(length):
        
        #id
        x1 = ''
        if(i==0):
            x1 = d[i]
        
        #title
        x2 = ''
        if(i==1):
            x2 = d[i]
        
        #author
        x3 = ''
        if(i==2):
            x3 = d[i]
        
        yield str(x1)+str(x2)+str(x3)
    

def load(s):
    print(s)
        

def get_graph():
    return bonobo.Graph(extract, transform, load)


if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser):
        bonobo.run(get_graph())
