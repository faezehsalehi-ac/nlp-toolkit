import re

class TextCleaner:
    def remove_html(self, text):
        return re.sub(r'<[^>]+>', '', text)
    
    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)