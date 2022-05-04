'''
PURPOSE:

'''
class Exporter:
    pass

class Websites_List:
    def __init__(self, sites_type):
        self.sites_type = sites_type
        self.websites = []

    def add(self, website):
       self.websites.append(website)
    
    def delete(self, website):
        self.websites.pop(website)

class Website:
    name: str = ''
    uname: str = ''
    pword: str = ''
    url: str = ''
    def __init__(self, name, uname, pword, url):
        self.name = name
        self.uname = uname
        self.pword = pword
        self.url = url

facebook = Website('facebook', 'test@facebook.com', 'fbookpword', 'www.facebook.com')
Websites_List.add(facebook)

print(Websites_List)
print(facebook)
