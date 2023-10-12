from modules.interaction_modules import fetch_data, verify_response, get_data_count


def initiate_interaction_module():
    score = 0
    total_items = get_data_count()

    for i in range(total_items):
        print(f"Fråga {i + 1}:")
        question, options = fetch_data(i)
        print(question)
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        user_response = input("Välj ett alternativ: ")

        if verify_response(
            i, int(user_response) - 1
        ):  # adjust the response to match zero-indexed options
            print("Korrekt!")
            score += 1
        else:
            print("Inkorrekt.")

    print(f"Du fick {score} av {total_items} rätt.")


if __name__ == "__main__":
    initiate_interaction_module()
