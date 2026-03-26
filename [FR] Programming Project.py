import pandas as pd
Hacker_MovesList = [[1,"DDos Attack", "15 Energy","Inflicts 20 Damage to the SysAdmin"],[2, "Phising Scam","10 HP","Restores 20 Energy (Capped at 100)"],[3, "Stealth Mode","10 Energy","Blocks SysAdmin's Firewall purge"]]
SysAdmin_MovesList = [[1,"Firewall Purge", "15 Energy","Inflicts 20 Damage (Blocked by Stealth)"],[2, "Reboot system","10 HP","Restores 20 Energy (Capped at 100)"],[3, "Trace Route","10 Energy","Inflicts 10 damage; Bypasses Stealth"]]
Hacker_Table = pd.DataFrame(Hacker_MovesList, columns=["Choice","Move","Cost","Effect"])
SysAdmin_Table = pd.DataFrame(SysAdmin_MovesList, columns=["Choice","Move","Cost","Effect"])
message ="Write fancy message here"
introduction = (f"""Welcome to Cyber Duel

{message}

{Hacker_Table}

{SysAdmin_Table}
""")
print(introduction)
Hacker = input("Hacker, who are you? ")
SysAdmin = input("SysAdmin, Who are you? ")

def game():
    Henergy = 30
    HHealth = 100
    Senergy = 30
    SHealth = 100
    roundCount = 1
    death = 0
    Energy_Health = [["", "Energy (EN)", f"{Henergy}", " | ", "", "Energy (EN)", f"{Senergy}"],
                     ["", "Health (HP)", f"{HHealth}", " | ", "", "Health (HP)", f"{SHealth}"]]
    Statistics = pd.DataFrame(Energy_Health, columns=[f"{Hacker}", "", "", " | ", f"{SysAdmin}", "", ""])
    print("Let the games begin")
    print(Statistics)
    while HHealth > 0 and SHealth > 0:
        Turn = roundCount % 2
        OverHeat = roundCount % 3

        if OverHeat == 0:

            print("""               Warning: OVERHEAT
                    -10 Health to players""")
            SHealth -= 10
            HHealth -= 10
            Energy_Health = [["", "Energy (EN)", f"{Henergy}", " | ", "", "Energy (EN)", f"{Senergy}"],
                             ["", "Health (HP)", f"{HHealth}", " | ", "", "Health (HP)", f"{SHealth}"]]
            Statistics = pd.DataFrame(Energy_Health, columns=[f"{Hacker}", "", "", " | ", f"{SysAdmin}", "", ""])
            print(Statistics)
            roundCount += 1
        elif Turn != 0 and OverHeat != 0:
            Hove = input(f"What will {Hacker} do? ")
            if int(Hove) < 100 or int(Hove) > 999:
                print("Please only enter 3 integers")
            else:
                x = Hove.count("1")
                y = Hove.count("2")
                z = Hove.count("3")
                # print(x, y, z)
                if x == 0 and y == 0 and z == 0:
                    print("Wow. That did nothing")

                if "1" in Hove:
                    if Henergy >= (x * 15):
                        print(f"{Hacker} used DDos Attack")
                        Henergy = Henergy - (x * 15)
                        SHealth = SHealth - (x * 20)
                    elif Henergy >= ((x - 1) * 15):
                        print(f"{Hacker} used DDos Attack")
                        Henergy = Henergy - ((x - 1) * 15)
                        SHealth = SHealth - ((x - 1) * 20)
                    elif Henergy >= ((x - 2) * 15):
                        print(f"{Hacker} used DDos Attack")
                        Henergy = Henergy - ((x - 2) * 15)
                        SHealth = SHealth - ((x - 2) * 20)
                    elif Henergy < 15:
                        print(f"{Hacker}, you can't use that. You could only perform Phising Scam (2)")

                if "2" in Hove:
                    if Henergy < 100:
                        print(f"{Hacker} used Phising Scam")
                        Henergy = Henergy + (y * 20)
                        HHealth = HHealth - (y * 10)
                    else:
                        print(f"{Hacker} can't use that! Energy only up to 100")
                        roundCount += 1
                if "3" in Hove:
                    if Henergy < 10:
                        print(f"{Hacker} can't use stealth mode")
                    elif Henergy >= (z * 10):
                        print(f"{Hacker} used Stealth Mode")
                        Henergy = Henergy - ((z - 2) * 10)
                    elif Henergy >= ((z - 2) * 10):
                        print(f"{Hacker} used Stealth Mode")
                        Henergy = Henergy - (z * 10)
                    elif Henergy >= ((z - 1) * 10):
                        print(f"{Hacker} used Stealth Mode")
                        Henergy = Henergy - ((z - 1) * 10)
                Energy_Health = [["", "Energy (EN)", f"{Henergy}", " | ", "", "Energy (EN)", f"{Senergy}"],
                                 ["", "Health (HP)", f"{HHealth}", " | ", "", "Health (HP)", f"{SHealth}"]]
                Statistics = pd.DataFrame(Energy_Health, columns=[f"{Hacker}", "", "", " | ", f"{SysAdmin}", "", ""])
                print(Statistics)

            roundCount += 1

        elif Turn == 0 and OverHeat != 0:
            Sove = input(f"What will {SysAdmin} do? ")
            if int(Sove) < 100 or int(Sove) > 999:
                print("Please only enter 3 integers")
            else:
                a = Sove.count("1")
                b = Sove.count("2")
                c = Sove.count("3")
                # print(x, y, z)
                if a == 0 and b == 0 and c == 0:
                    print("Aww. You wasted a turn")

                if "3" in Sove:
                    if Senergy <= 10:
                        print(f"{SysAdmin} don't have enough energy")
                    elif Senergy > (c * 10):
                        print(f"{SysAdmin} used Trace Route")
                        Senergy = Senergy - (c * 10)
                        HHealth = HHealth - (c * 10)
                        z = 0
                    elif Senergy > ((c - 1) * 10):
                        print(f"{SysAdmin} used Trace Route")
                        Senergy = Senergy - ((c - 1) * 10)
                        HHealth = HHealth - ((c - 1) * 10)
                        z = 0
                    elif Senergy > ((c - 2) * 10):
                        print(f"{SysAdmin} used Trace Route")
                        Senergy = Senergy - ((c - 2) * 10)
                        HHealth = HHealth - ((c - 2) * 10)
                        z = 0
                if "1" in Sove:
                    if Senergy < 15:
                        print(f"{SysAdmin} doesn't have enough energy")
                    else:
                        if z == 0:
                            if Senergy >= (a * 15):
                                print(f"{SysAdmin} used Firewall Purge")
                                Senergy = Senergy - (a * 15)
                                HHealth = HHealth - (a * 20)
                            elif Senergy >= ((a - 1) * 15):
                                print(f"{SysAdmin} used Firewall Purge")
                                Senergy = Senergy - ((a - 1) * 15)
                                HHealth = HHealth - ((a - 1) * 20)
                            elif Senergy >= ((a - 2) * 15):
                                print(f"{SysAdmin} used Firewall Purge")
                                Senergy = Senergy - ((a - 2) * 15)
                                HHealth = HHealth - ((a - 2) * 20)
                        if z > 0:
                            print(f"Blocked by {Hacker}'s Stealth Mode")
                if "2" in Sove:
                    if Senergy < 100:
                        print(f"{SysAdmin} used Reboot System")
                        Senergy = Senergy + (b * 20)
                        HHealth = HHealth - (b * 10)
                    else:
                        print(f"{SysAdmin}, you can't use that! Energy only up to 100")
                Energy_Health = [["", "Energy (EN)", f"{Henergy}", " | ", "", "Energy (EN)", f"{Senergy}"],
                                 ["", "Health (HP)", f"{HHealth}", " | ", "", "Health (HP)", f"{SHealth}"]]
                Statistics = pd.DataFrame(Energy_Health, columns=[f"{Hacker}", "", "", " | ", f"{SysAdmin}", "", ""])
                print(Statistics)
            roundCount += 1

    Energy_Health = [["", "Energy (EN)", f"{Henergy}", " | ", "", "Energy (EN)", f"{Senergy}"],
                     ["", "Health (HP)", f"{HHealth}", " | ", "", "Health (HP)", f"{SHealth}"]]
    Statistics = pd.DataFrame(Energy_Health, columns=[f"{Hacker}", "", "", " | ", f"{SysAdmin}", "", ""])
    if HHealth <= 0 or SHealth <= 0:
        if HHealth <= 0 and SHealth <= 0:
            print("Double K.O.")
        if HHealth <= 0 and SHealth > 0:
            print(f"{SysAdmin} wins")
        if SHealth <= 0 and HHealth > 0:
            print(f"{Hacker} wins")

    Continue = int(input("""Do you wish to continue? 
            1 - Rematch
            2 - Finish

                -->"""))
    if Continue == 1:
        print("Rematch confirmed")
        Henergy = 30
        HHealth = 100
        Senergy = 30
        SHealth = 100
        roundCount = 1
        death = 0
        print(introduction)
        game()
    elif Continue == 2:
        print("Game Over")
game()
