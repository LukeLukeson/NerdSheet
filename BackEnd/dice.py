# Dice Rolling Class

import random

class dice:

    def roll(self, type, abilityScore):
        self.type = type
        self.abilityScore = abilityScore

        # Roll D20
        if type == 20:
            
            twenty = random.randint(1,20)
            if twenty == 20:
                print('Natural 20')
            elif twenty == 1:
                print('Critical Fail')
            else:
                twentyFinal = twenty + int(abilityScore)
                print(str(twenty) + ' + ' + str(abilityScore) + ' = ' + str(twentyFinal)) 
                
        # Roll D12
        elif type == 12:

            twelve = random.randint(1,12)
            twelvefinal = twelve + int(abilityScore)
            print(str(twelve) + ' + ' + str(abilityScore) + ' = ' + str(twelvefinal))

        # Roll D10
        elif type == 10:

            ten = random.randint(1,10)
            tenfinal = ten + int(abilityScore)
            print(str(ten) + ' + ' + str(abilityScore) + ' = ' + str(tenfinal))
        # Roll D100
        elif type == 100:

            hundred = random.randint(1,100)
            hundredfinal = hundred + int(abilityScore)
            print(str(hundred) + ' + ' + str(abilityScore) + ' = ' + str(hundredfinal))
        # Roll D8
        elif type == 8:

            eight = random.randint(1,8)
            eightfinal = eight + int(abilityScore)
            print(str(eight) + ' + ' + str(abilityScore) + ' = ' + str(eightfinal))
        # Roll D6
        elif type == 6:

            six = random.randint(1,6)
            sixfinal = six + int(abilityScore)
            print(str(six) + ' + ' + str(abilityScore) + ' = ' + str(sixfinal))
        # Roll D4
        elif type == 4:

            four = random.randint(1,4)
            fourfinal = four + int(abilityScore)
            print(str(four) + ' + ' + str(abilityScore) + ' = ' + str(fourfinal))
        # Roll D2
        elif type == 2:

            two = random.randint(1,2)
            twofinal = two + int(abilityScore)
            print(str(two) + ' + ' + str(abilityScore) + ' = ' + str(twofinal))
        # Not a valid die
        else:
            print('Thats not a valid die')