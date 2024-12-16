
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")


voices = speaker.GetVoices()


print("Available voices:")
for i in range(voices.Count):
    print(f"{i}: {voices.Item(i).GetDescription()}")


try:
    voice_index = int(input("Enter the index of the voice you want to use: "))
    if 0 <= voice_index < voices.Count:
        speaker.Voice = voices.Item(voice_index)
        print(f"Voice changed to: {voices.Item(voice_index).GetDescription()}")
    else:
        print("Invalid index. Using default voice.")
except ValueError:
    print("Invalid input. Using default voice.")


print("Enter the word you want to be spoken out by the computer")
print("Type 'exit' to stop the program.")

while True:
    s = input("> ")
    if s.strip().lower() == 'exit':
        break
    speaker.Speak(s)

print("Program ended.")
