# Dice Rolling Class

import random

class dice:

    def roll(self, type, abilityScore):
        
        self.type = type
        self.abilityScore = abilityScore

        if type == 20:
            
            twenty = random.randint(1,20)
            if twenty == 20:
                print('Natural 20')
            elif twenty == 1:
                print('Critical Fail')
            else:
                twentyFinal = twenty + int(abilityScore)
                print(str(twenty) + ' + ' + str(abilityScore) + ' = ' + str(twentyFinal)) 

        elif type == 12:

            twelve = random.randint(1,12)
            twelvefinal = twelve + int(abilityScore)
            print(str(twelve) + ' + ' + str(abilityScore) + ' = ' + str(twelvefinal))