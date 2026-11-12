
def implies(a, b):
    return not a or b

def evaluate(expr, model):
    expr = expr.replace(" ", "")

    if expr == "Q->P":
        return implies(model["Q"], model["P"])
    if expr == "P->NOTQ":
        return implies(model["P"], not model["Q"])
    if expr == "QORR":
        return model["Q"] or model["R"]
    if expr == "R":
        return model["R"]
    if expr == "R->P":
        return implies(model["R"], model["P"])
    if expr == "Q->R":
        return implies(model["Q"], model["R"])

    return False

def check_all(kb, query, symbols, model):
    if len(symbols) == 0:
        if all(evaluate(s, model) for s in kb):
            return evaluate(query, model)
        return True

    p = symbols[0]

    m1 = model.copy()
    m1[p] = True

    m2 = model.copy()
    m2[p] = False

    return (check_all(kb, query, symbols[1:], m1) and
            check_all(kb, query, symbols[1:], m2))

def tt_entails(kb, query, symbols):
    return check_all(kb, query, symbols, {})

# MAIN
kb = ["Q->P", "P->NOTQ", "QORR"]
symbols = ["P", "Q", "R"]

query = input("Enter query (R / R->P / Q->R): ").strip()

if query not in ["R", "R->P", "Q->R"]:
    print("Invalid query")
else:
    if tt_entails(kb, query, symbols):
        print("KB entails the query: TRUE")
    else:
        print("KB does not entail the query: FALSE")