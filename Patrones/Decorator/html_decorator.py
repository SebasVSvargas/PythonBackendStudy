from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def print(self):
        pass

class SimpleText(Text):
    def __init__(self, content):
        self._content = content

    def print(self):
        return self._content
    
class TextDecorator(Text):
    def __init__(self, text: Text):
        self._text = text

    def print(self):
        return self._text.print()
    
class BoldText(TextDecorator):
    def print(self):
        return f"<b>{self._text.print()}</b>"

class ItalicText(TextDecorator):
    def print(self):
        return f"<i>{self._text.print()}</i>"    
    
class UnderlinedText(TextDecorator):
    def print(self):
        return f"<u>{self._text.print()}</u>"   
    
text = SimpleText("Hola Cabezon")
print(f"{text.print()}")
print("--------------------")

bold_text = BoldText(text)
print(f"{bold_text.print()}")
print("--------------------")

italic_text = ItalicText(bold_text)
print(f"{italic_text.print()}")
print("--------------------")

underline_text = UnderlinedText(italic_text)
print(f"{underline_text.print()}")
print("--------------------")