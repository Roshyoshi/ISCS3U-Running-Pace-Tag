
def printPaceTime(i, s):
    h =int(int(s)/ int(3600))
    ms = s%3600
    m = int(int(ms)/int(60))
    s = ms%60
    print( f"{i:02d}\t{h:02d}:{m:02d}:{s:02d} ")


def main():
    runnerName = ""
    while runnerName == "":
        runnerName = input("Enter your name: ")

    distanceUnits = {"kilometers": 1.0, "miles": 0.62}

    distanceUnit = ""

    while True:
        distanceUnit = input("Enter Kilometers or Miles: ").lower()
        if distanceUnit not in distanceUnits:
            print("Invalid Selection.")
            continue
        else:
            break

    upperbound = int(distanceUnits[distanceUnit] * 100.0)
    while True:
        try:
            distance = int(input("Enter distance in " + distanceUnit + ": "))
            if distance >= upperbound or distance < 1.0:
                print(f"Must be between {upperbound} and 1")
                continue
            break
        except:
            print("Invalid Distance.")
            continue

    while True:
        try:
            goalTime = str(input("Enter your Goal Time (format: HHMMSS): "))
        except:
            print("Please enter a valid numerical Goal.")
            continue

        if not len(goalTime) == 6 or int(goalTime) == 0:
            print("Invalid Goal.")
            continue

        valid = True
        hours = int(goalTime[0:2])
        if hours < 0 or hours > 23:
            print("Invalid hours.")
            valid = False

        minutes = int(goalTime[2:4])
        if minutes < 0 or minutes > 59:
            print("Invalid minutes.")
            valid = False

        seconds = int(goalTime[4:6])
        if seconds < 0 or seconds > 59:
          print("Invalid seconds.")
          valid = False

        if (valid):
          break
        else:
          print("Try again.")
          continue


    shortenedDistanceUnits = {"kilometers": "km", "miles": "mi"}

    print(f"\n{runnerName}'s Pace Tag")
    print(
        f"Distance = {distance}{shortenedDistanceUnits[distanceUnit]}, Goal Time = {hours}:{minutes}:{seconds}")
    print(f"{shortenedDistanceUnits[distanceUnit]}\tElapsed Time")

    secondsPerKilo = (hours * 3600 + minutes * 60 + seconds)/distance

    for i in range(1, distance + 1):
        printPaceTime(i, int(i * secondsPerKilo))





if __name__ == "__main__":
  main()
