


class ExtensionMixin:

    def add_extension(self, title):
        self.extensions.append(title)
        return f'Добавлено новое расширение {title} для игры {self.name}.'
    
    def remove_extension(self, title):
        if title in self.extensions:
            self.extensions.remove(title)
            return f'{title} был отключен от {self.name}'
        
        return 'Такого расширения нет в списке.'
    

class Game(ExtensionMixin):
    def __init__(self, type_, name):
        self.type = type_
        self.name = name
        self.extensions = []

    def get_description(self, description):
        return f'{self.name} это {description}'
    
    def get_extensions(self):
        if self.extensions:
            return ' '.join(self.extensions)
        return 'Нет подключенных расширений'