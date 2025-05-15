def parse(input: str) -> str:
    input = input.strip()

    if input.endswith("@@fix"):
        return f"Return only the fixed text, no other text or comments. Make sure that the meaning is not changed and the tone is not changed.Fix the grammar, spelling, and fluency of the following text: \n{input[:-5].strip()}"
    
    return input
