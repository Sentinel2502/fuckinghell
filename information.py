"""инормация для игры"""

from gameObject import *
from locations import *
from textObject import *

#cписок локаций
locationObjectsList = {
"bedroom": LocationObject((1024, 768), pygame.image.load("images/locations/bedroom.png")),
"library": LocationObject((1024, 768), pygame.image.load("images/locations/library.png"))}


#СПАЛЬНЯ
bedroomIntersectionObjectsList = [GameObject(13, 550, 280, 204)]
bedroomTextObjectsList = [TextObject(None, 30, (255, 255, 255), "Грусть, печаль, тоска", 1, bedroomIntersectionObjectsList[0])]
bedroomExitObjectsList = [[GameObject(264, 153, 109, 223), "library"]]

locationObjectsList["bedroom"].setGameField(GameObject(0, 374, 1024, 374))
locationObjectsList["bedroom"].setIntersectionObjectsList(bedroomIntersectionObjectsList)
locationObjectsList["bedroom"].setExitObjectsList(bedroomExitObjectsList)
locationObjectsList["bedroom"].setExitPoint((268, 384))
locationObjectsList["bedroom"].setTextObjectsList(bedroomTextObjectsList)


#БИБЛИОТЕКА
libraryIntersectionObjectsList = [GameObject(164, 459, 383-164, 593-459)]
libraryExitObjectsList = [[GameObject(271, 752, 600, 100), "bedroom"]]
libraryTextObjectsList = [TextObject(None, 30, (255, 255, 255), "Грусть, печаль, тоска", 1, libraryIntersectionObjectsList[0])]

locationObjectsList["library"].setGameField(GameObject(60, 400, 905, 367))
locationObjectsList["library"].setIntersectionObjectsList(libraryIntersectionObjectsList)
locationObjectsList["library"].setExitObjectsList(libraryExitObjectsList)
locationObjectsList["library"].setExitPoint((306, 680))
locationObjectsList["library"].setTextObjectsList(libraryTextObjectsList)
