from datetime import datetime
import calendar
import ast


class Gate:
    champion=""
    date_intervals=[]

    def __init__(self, champion, date_intervals):
        self.champion=champion
        self.date_intervals=date_intervals

    def invincible_days(self, date):
        invincible_days=calendar.day_name[date.weekday()]
        if str(invincible_days) == "Tuesday" or str(invincible_days) == "Thursday":
            return True
        else:
            return False

    def calc_damage(self, date, champion):
        if self.invincible_days(date):
            return 0, "Holly days"
        elif self.no_damage_creatures(champion):
            return 0, "Champion " + champion.upper() + " is invincible"

        # "Janna" demon of Wind
        if date.hour == 6 and 0 <= date.minute <= 29:
            return 7, 'Attacked by "Janna" demon of Wind'
        # "Tiamat" goddess of Oceans
        elif date.hour == 6 and 30 <= date.minute <= 59:
            return 18, 'Attacked by "Tiamat" goddess of Oceans'
        # "Mithra" goddess of sun
        elif date.hour == 7 and 0 <= date.minute <= 59:
            return 25, 'Attacked by "Mithra" goddess of sun'
        # "Warwick" god of war
        elif date.hour == 8 and 0 <= date.minute <= 29:
            return 18, 'Attacked by "Warwick" god of war'
        # "Kalista" demon of agony
        elif 8 <= date.hour <= 14 and 30 <= date.minute <= 59:
            return 7, 'Attacked by "Kalista" demon of agony'
        # "Ahri" goddess of wisdom
        elif date.hour == 15 and 0 <= date.minute <= 29:
            return 13, 'Attacked by "Ahri" goddess of wisdom'
        # "Brand" god of fire
        elif date.hour == 15 and date.minute >= 0 or date.hour == 16 and date.minute <= 59:
            return 25, 'Attacked by "Brand" god of fire'
        # "Rumble" god of lightning
        elif date.hour == 17 and 0 <= date.minute <= 59:
            return 18, 'Attacked by "Rumble" god of lightning'
        # "Skarner" the scorpion demon
        elif 18 <= date.hour <= 19 and 0 <= date.minute <= 59:
            return 7, 'Attacked by "Skarner" the scorpion demon'
        # "Luna" the goddess of the moon
        elif date.hour == 20 and date.minute <= 59:
            return 13, 'Attacked by "Luna" the goddess of the moon'
        else:
            return 0, 'Nobody guarding the gate ('+ str(date)+ ')'

    def no_damage_creatures(self, champion):
        return champion == 'wizard' or champion == 'spirit'

    def calc_health(self, champion, date_intervals):
        if self.no_damage_creatures(champion):
            return 100, "Champion " + champion.upper() + " is invincible"

        attacked = ''
        date=datetime.strptime(date_intervals[0], "%Y-%m-%d %H:%M")
        total_damage, attacked=self.calc_damage(date, champion)

        if date_intervals.__len__() > 1:
            for date_string in date_intervals[1:]:
                date_next=datetime.strptime(date_string, "%Y-%m-%d %H:%M")
            if (date_next - date).total_seconds() > 3600:
                date=date_next

                next_damage, attacked1=self.calc_damage(date, champion)
                total_damage += next_damage
                attacked = attacked + "," + attacked1

            else:
                raise ValueError("Champion can be attacked only one every hour")

        if champion.lower() == 'giant':
            return 150 - total_damage, attacked
        elif champion.lower() == 'vampire':
            return 110 - total_damage, attacked
        else:
            return 100 - total_damage, attacked

    def isValidDatetime(self, intervals):
        try:
            intervals=ast.literal_eval(date_string_intervals)
            for i in intervals:
                datetime.strptime(i, "%Y-%m-%d %H:%M")
            return True
        except:
            return False


if __name__ == '__main__':

    while True:
        try:
            listOfValidChampions=['wizard', 'human', 'spirit', 'giant', 'vampire']

            # Validate If the user provides a valid champion
            champion=input("Please enter the champion you want to send to the gate: ").strip().lower()
            while champion not in listOfValidChampions:
                print("Valid Champions list: ", listOfValidChampions)
                champion=input("Please enter the champion you want to send to the gate: ").lower()

            # Get date string intervals from user
            date_string_intervals=input("Please enter date interval strings in ['YYYY-MM-DD HH:MM', 'YYYY-MM-DD "
                                        "HH:MM'] format: ").strip()

            # instantiate a GATE object
            gate_object=Gate(champion, date_string_intervals)

            # validate date string intervals
            while True:
                if not gate_object.isValidDatetime(date_string_intervals):
                    print("Invalid date time string intervals")
                    date_string_intervals=input(
                        "Please enter date interval strings in ['YYYY-MM-DD HH:MM', 'YYYY-MM-DD "
                        "HH:MM'] format: ").strip()
                else:
                    break

            # valid date sting intervals
            date_string_intervals=ast.literal_eval(date_string_intervals)

            # Calculate the total damage of a champion as per user provided date string intervals
            total_damage, attacked_by=gate_object.calc_health(champion, date_string_intervals)
            print('The total health that is remained at the end of the game for ' + str(champion) + ' is: ' + str(
                total_damage) + ". [" + str(attacked_by) + "]")

        except ValueError as err:
            print(err)
