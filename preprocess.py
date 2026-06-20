from music21 import converter, note, chord
import os
import pickle

notes = []

for file in os.listdir("dataset"):
    if file.endswith(".mid"):
        print("Reading:", file)

        midi = converter.parse(os.path.join("dataset", file))

        for element in midi.flatten().notes:

            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

print("Total Notes Found:", len(notes))

with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("Notes saved successfully!")