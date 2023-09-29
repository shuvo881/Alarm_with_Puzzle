import winsound

# Define the frequency and duration of the beep sound
frequency = 1000  # Frequency in Hertz (1000Hz = 1kHz)
duration = 1000   # Duration in milliseconds (1 second)

# Infinite loop to play the beep sound


def alarm():
    while True:
        winsound.Beep(frequency, duration)



