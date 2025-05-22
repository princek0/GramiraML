def parse(input: str) -> str:
    input = input.strip()

    if input.endswith("@@fix"):
        prompt = "Improve the grammar and spelling of the provided text. Only reply with the improved text. Do not reply with anything else but the improved text. Do not include @@fix in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    return input
