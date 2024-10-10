from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
# print(Implication(AKnight,AKnave))
# Puzzle 0
# A says "I am both a knight and a knave."
# print(And(AKnave,Not(AKnight)))
# print(And(Or(Not(AKnight),AKnave),Or(AKnight,Not(AKnave))))
knowledge0 = And(
    # TODO
    # AKnight,AKnave
    # AKnave
    # Biconditional(AKnight,Not(AKnave)),
    Or(AKnight,AKnave),
    # Or(AKnave,AKnight),
    Not(And(AKnave,AKnight)),
    # # Or(Knight),
    Implication(AKnave,Not(And(AKnight,AKnave))),
    Implication(AKnight,And(AKnight,AKnave))


)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
#    Or(AKnight,AKnave)
    # Not(AKnight)
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave, BKnight)),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    Or(AKnave,AKnight),
    Or(BKnave,BKnight),
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Implication(AKnave,Or(And(AKnave,BKnight),And(AKnight,BKnave))),
    Implication(AKnight,Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Implication(BKnave,Or(And(AKnave,BKnight),And(AKnight,BKnave))),
    Implication(BKnight,Or(And(AKnave,BKnight),And(AKnight,BKnave))),
    # BKnight
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    # CKnight,
    Not(And(AKnave,AKnight)),
    Not(And(BKnave,BKnight)),
    Not(And(CKnave,CKnight)),
    Implication(AKnight,Or(AKnight,AKnave)),
    Implication(AKnave,Not(Or(AKnight,AKnave))),

    Implication(BKnight,AKnave),
    Implication(BKnave,AKnight),
    Implication(BKnight,CKnave),
    # BKnave,
    Implication(BKnave,CKnight),
    Implication(CKnight,AKnight),

    Implication(CKnave,Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
