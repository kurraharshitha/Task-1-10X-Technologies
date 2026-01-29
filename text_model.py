from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Loading open-source text model...")

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting...")
        break

    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=80
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Model:", answer)
    print()