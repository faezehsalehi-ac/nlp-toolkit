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
    
    def remove_extra_spaces(self, text):
        return re.sub(r'\s+', ' ', text).strip()
    
    def clean(self, text, remove_numbers=False, keep_words=None):

        if keep_words is None:
            keep_words = []
        
        placeholders = {}
        for word in keep_words:
            placeholder = f"KEEP{word}KEEP"
            placeholders[placeholder]  = word
            text = text.replace(word, placeholder)

        text = self.remove_html(text)
        
        if remove_numbers:
            text = self.remove_numbers(text)

        
        text = self.remove_punctuation(text)
        text = self.to_lowercase(text)
        text = self.remove_extra_spaces(text)


        for placeholder, word in placeholders.items():

            temp = placeholder
            temp = self.remove_punctuation(temp)
            temp = self.to_lowercase(temp)

            text = text.replace(placeholder.lower(), word)




        return text
    
    