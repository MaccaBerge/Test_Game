import pygame
from typing import Union

class Animation():
    def __init__(self, images: list, duration: Union[float, int], loop: bool = True) -> None:
        self.images = images
        self.duration = duration
        self.loop = loop
        self.done = False
    
    def update(self) -> None:
        pass


l1 = ['One', 2, False]

l2 = l1.copy()

print(l1, l2)

l2[2] = True

print(l1, l2)