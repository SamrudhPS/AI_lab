def model_based_agent(location, status):

    if not hasattr(model_based_agent, "internal_state"):
        model_based_agent.internal_state = {
            "A": "Unknown",
            "B": "Unknown"
        }

    model_based_agent.internal_state[location] = status

    if status == "Dirty":
        return "Suck"

    elif (model_based_agent.internal_state["A"] == "Clean"
          and model_based_agent.internal_state["B"] == "Clean"):
        return "Stop"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"

print("Output:")

print(model_based_agent("A", "Dirty"))
print(model_based_agent("A", "Clean"))
print(model_based_agent("B", "Dirty"))
print(model_based_agent("B", "Clean"))