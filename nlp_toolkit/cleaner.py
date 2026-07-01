import re

class TextCleaner:
    def remove_html(self, text):
        return re.sub(r'<[^>]+>', '', text)
    
    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)
    
    def remove_numbers(self, text):
        return re.sub(r'\d+', '', text)
    
    def to_lowercase(self, text):
        return text.lower()
    
    def clean(self, text, remove_numbers=False):
        text = self.remove_html(text)
        
        if remove_numbers:
            text = self.remove_numbers(text)

        
        text = self.remove_punctuation(text)
        text = self.to_lowercase(text)
        text = self.remove_extra_spaces(text)
        return text
    
    def remove_extra_spaces(self, text):
        return re.sub(r'\s+', ' ', text).strip()