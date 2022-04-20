#Site summary class intended to summarize the details of a website

class SiteSummary:
    def __init__( 
        self, title, url, text_length, html_length, \
        layout, full_text, full_html):
        self.title = title
        self.url = url
        self.text_length = text_length
        self.html_length = html_length
        self.layout = layout
        self.full_text = full_text
        self.full_html = full_html

    def addsitesummary(self, title, url):
        pass
    
    def getsitesummary(self, url):
        pass