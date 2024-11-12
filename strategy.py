from math import sqrt
from math import dist

class RouteStrategy():
    
    def buildRoute(A,B):
        return(A+B)

class RoadStrategy(RouteStrategy):    
    def buildRoute(A, B):
        roadDistance = 1/4*dist(A,B)
        return(roadDistance)
    
class PublicTransportStrategy(RouteStrategy):
    def buildRoute(A, B):
        x = max(A[0],B[0]) - min(A[0],B[0])
        y = max(A[1],B[1]) - min(A[1],B[1])
        PTDistance = 1/2*sqrt((x)**2 + y**2)
        return(PTDistance)

class WalkingStrategy(RouteStrategy):
    def buildRoute(A, B):
        walkingDistance = dist(A,B)
        return (walkingDistance)

class Navigator():
    def __init__(self, routeStrat = "unknown"):
        self.routeStrategy = routeStrat
        
    def buildRoute(self, A,B):
        if self.routeStrategy == "unknown":
            route = RouteStrategy.buildRoute(A,B)
            
        elif self.routeStrategy == "walking":
            route = WalkingStrategy.buildRoute(A,B)
            
        elif self.routeStrategy == "public transit":
            route = PublicTransportStrategy.buildRoute(A,B)
        
        elif self.routeStrategy == "driving":
            route = RoadStrategy.buildRoute(A,B)
        
        print(route)    
        
A = (1,1)
B = (4,5)
publicTransit = Navigator("public transit")
publicTransit.buildRoute(A,B)