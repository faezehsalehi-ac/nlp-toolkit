import re

class TextCleaner:
    def remove_html(self, text):
        return re.sub(r'<[^>]+>', '', text)
    
    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)
    
    def remove_numbers(self, text):
        return re.sub(r'\d+', '', text)
    
    def to_lowecase(self, text):
        return text.lower()
    
    def clean(self, text):
        text = self.remove_html(text)
        text = self.remove_numbers(text)
        text = self.remove_punctuation(text)
        text = self.to_lowecase(text)
        return text
    
    def remove_extra_spaces(self, text):
        return re.sub(r'\s+', '', text).strip()