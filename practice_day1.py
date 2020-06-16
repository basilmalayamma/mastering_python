
def get_signal_strength(signal):
    signal_strength = []
    for signals in signal:
        if(signals < 60):
            signal_strength.append("EXCELLENT")
        elif(60 <= signals < 80):
            signal_strength.append("GOOD")
        elif(80 <= signals < 90):
            signal_strength.append("POOR")
        else:
            signal_strength.append("UNREACHABLE")
    return signal_strength

def main():
    device = ["Thermostat","door lock", "motion sensor", "Smoke Alarm", "Water Level Sensor"]
    signal = [48.5, 94.5, 44.5, 78, 24]
    signal_strength = get_signal_strength(signal)
    for i in range(0, len(device)):
        print("{0}: {1}".format(device[i],signal_strength[i]))

if __name__ == "__main__":
    main()
