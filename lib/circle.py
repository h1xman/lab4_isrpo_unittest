import math


def area(r):
    '''
    Возвращает площадь круга заданного радиуса.
    
        Args:
            r (float): радиус круга

        Returns:
            circle_area (float):  площадь круга радиуса r
    
        Examples:
            area(2.3)      # -> ~ 16.62
    '''
    
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга заданного радиуса.
    
        Args:
            r (float): радиус круга

        Returns:
            circle_perimeter (float):  периметр круга радиуса r

        Examples:
            perimeter(2.3)      # -> ~ 14.45
    '''

    return 2 * math.pi * r


