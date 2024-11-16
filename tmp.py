# List of sentences
import json
name = 'Llama-2-7b-hf_raw'
#name = 'StructLM-7B-M2-D2'

folder = 'Llama-2-7b-hf'

with open(f"./Outputs/{folder}/{name}.json", 'r') as f:
    data = json.load(f)
print(len(data["Prompt"]), len(data["Original"]), len(data["Prediction"]))

sentences = data["Prompt"]

# Dictionary to store the index of each duplicate sentence
duplicates = {}
seen_sentences = set()

# Detect duplicates and store indices
for index, sentence in enumerate(sentences):
    if sentence in seen_sentences:
        # Append the index if the sentence is a duplicate
        duplicates[sentence].append(index)
    else:
        # First occurrence of the sentence
        seen_sentences.add(sentence)
        duplicates[sentence] = [index]

# Filter to keep only the sentences with duplicates
duplicate_indices = {sentence: indices for sentence, indices in duplicates.items() if len(indices) > 1}

# Display results
print("Indices of duplicated sentences:")
indices_to_delete = []
for sentence, indices in duplicate_indices.items():
    # Collect indices to delete
    indices_to_delete_ = indices[1:-1]
    # Delete in reverse order to avoid index errors
    indices_to_delete += sorted(indices_to_delete_, reverse=True)

# Delete duplicates
indices_to_delete = sorted(indices_to_delete, reverse=True)
#print("Indices to delete:", indices_to_delete)
def delete(sentences):
    for index in indices_to_delete:
        del sentences[index]
    return sentences

data["Prompt"] = delete(sentences)
data["Original"] = delete(data["Original"])
data["Prediction"] = delete(data["Prediction"])

print(len(data["Prompt"]), len(data["Original"]), len(data["Prediction"]))


with open(f"./Outputs/{folder}/{name}.json", 'w+') as f:
    json.dump(data, f, indent=4)