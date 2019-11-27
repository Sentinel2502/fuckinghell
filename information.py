from gameObject import *
from locations import *

locationObjectsList = {
"bedroom": LocationObject((1024, 768), pygame.image.load("images/locations/bedroom.png")),
"library": LocationObject((1024, 768), pygame.image.load("images/locations/library.png"))}

bedroomIntersectionObjectsList = [GameObject(13, 550, 280, 204)]
bedroomExitObjectsList = [[GameObject(264, 153, 109, 223), "library"]]

locationObjectsList["bedroom"].setGameField(GameObject(0, 374, 1024, 374))
locationObjectsList["bedroom"].setIntersectionObjectsList(bedroomIntersectionObjectsList)
locationObjectsList["bedroom"].setExitObjectsList(bedroomExitObjectsList)
locationObjectsList["bedroom"].setExitPoint((268, 384))


libraryIntersectionObjectsList = [GameObject(164, 459, 383-164, 593-459)]
libraryExitObjectsList = [[GameObject(271, 752, 600, 100), "bedroom"]]

locationObjectsList["library"].setGameField(GameObject(60, 400, 905, 367))
locationObjectsList["library"].setIntersectionObjectsList(libraryIntersectionObjectsList)
locationObjectsList["library"].setExitObjectsList(libraryExitObjectsList)
locationObjectsList["library"].setExitPoint((306, 680))
