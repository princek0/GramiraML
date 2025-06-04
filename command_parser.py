def parse(input: str) -> str:
    input = input.strip()

    if input.endswith("@@fix"):
        prompt = "Improve the grammar and spelling of the provided text. Only reply with the improved text. Do not reply with anything else but the improved text. Do not include @@fix in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@spanish"):
        prompt = "Translate the provided text to Spanish. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@spanish in your answer. Here is the provided text:"
        return f"{prompt}+{input}" 
    
    if input.endswith("@@genz"):
        prompt = "Translate the provided text to GenZ slang. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@genz in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@formal"):
        prompt = "Translate the provided text to formal language. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@formal in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@casual"):
        prompt = "Translate the provided text to casual language. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@casual in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@technical"):
        prompt = "Translate the provided text to technical language. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@technical in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@plain"):
        prompt = "Translate the provided text to plain language. Only reply with the translated text. Do not reply with anything else but the translated text. Do not include @@plain in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@shorten"):
        prompt = "Shorten the provided text. Only reply with the shortened text. Do not reply with anything else but the shortened text. Do not include @@shorten in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@expand"):
        prompt = "Expand the provided text. Only reply with the expanded text. Do not reply with anything else but the expanded text. Do not include @@expand in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@summarize"):
        prompt = "Summarize the provided text. Only reply with the summary. Do not reply with anything else but the summary. Do not include @@summarize in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    if input.endswith("@@paraphrase"):
        prompt = "Paraphrase the provided text. Only reply with the paraphrased text. Do not reply with anything else but the paraphrased text. Do not include @@paraphrase in your answer. Here is the provided text:"
        return f"{prompt}+{input}"
    
    return input
