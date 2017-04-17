from random import *

class Employee(object):
    def __init__(self, firstName, lastName):
        self.__first_name = firstName
        self.__last_name = lastName
        self.eateries = list(['McDonalds', 'Thai Food', 'Applebees', 'Martins', 'Taco Bell'])

    def eat(self, food = None, companions = None):
        numOfEateries = len(self.eateries)
        randSeed = randrange(0, numOfEateries)
        randomEatery = self.eateries[randSeed]
        tempString = self.__first_name + " " + self.__last_name
        tempCompanions = ' with '

        # Stingify the companions (if they exist)
        if companions:
            for index,person in enumerate(companions):
                if index == len(companions) - 1:
                    tempCompanions += 'and ' + person + '.'
                else:
                    tempCompanions += person + ', '

        # If food is given
        if food:
            if food[len(food)- 1] == 's':
                tempString += ' ate '
            # Handle 'a' and 'an' (depends on the first letter of food being a vowel/constanent)
            elif food[0] == 'a' or food[0] == 'e' or food[0] == 'i' or food[0] == 'o' or food[0] == 'u':
                tempString += ' ate an '
            else:
                tempString +=  ' ate a '


            tempString += food + " at " + randomEatery
            # If food AND companions are given
            if companions:
                tempString += tempCompanions
        else:
            tempString +=  ' ate at '  + randomEatery + tempCompanions
        print(tempString)
        return randomEatery



john = Employee('John', 'Smith')
jane = Employee('Jane', 'Doe')

john.eat('apple')
jane.eat('orange', ['Will','Alli','Sims'])











