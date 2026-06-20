import pickle
from music21 import stream, note

with open("generated_notes.pkl", "rb") as f:
    generated_notes = pickle.load(f)

music_stream = stream.Stream()

count = 0

for pattern in generated_notes:

    try:
        # Normal notes like D4, F#4, G3
        if any(letter in str(pattern) for letter in ["A","B","C","D","E","F","G"]):
            n = note.Note(pattern)
            n.offset = count * 0.5
            music_stream.append(n)
            count += 1

    except:
        pass

print("Notes added:", count)

music_stream.write("midi", fp="generated_music.mid")

print("MIDI created!")