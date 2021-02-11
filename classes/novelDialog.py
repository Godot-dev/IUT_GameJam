import pygame

class NovelDialog:
    def __init__(self, id, type, img, name, text, choices, next):
        self.id = id
        self.type = type
        self.img = "assets/backgroundVn/" + img
        self.name = name
        self.text = text
        self.choices = choices
        self.next = next

