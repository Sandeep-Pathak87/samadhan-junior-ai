# Project: Samadhan Junior - Phase 1
# Simple Logic for Playgroup Counting

def start_lesson():
    item = "Apple"
    color = "Red"
    count = 3

    print("--- Welcome to Samadhan Junior ---")
    print(f"I have some {color} {item}s 🍎🍎🍎")
    print(f"Can you count how many {item}s there are?")

    # In this phase, we just set the variables. 
    # In Phase 2, we add the AI to check the answer.
    return count

if __name__ == "__main__":
    correct_answer = start_lesson()
    print(f"(Internal Note: The correct answer is {correct_answer})")
