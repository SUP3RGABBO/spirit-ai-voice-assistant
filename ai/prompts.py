from config import assistant_name

starting_phrases = [
    "Yes sir, how can I assist you?",
    "I'm here, what can I do for you?",
    "At your service.",
    "Ready for action. What do you need?",
    "How can I help you today?"
]

continued_phrases = [
    "Yes?",
    "Go ahead.",
    "I'm listening.",
    "Here I am."
]

thinking_phrases = [
    "I'm thinking...",
    "One moment, I'm reflecting.",
    "I'm searching for information...",
    "Give me a moment to respond.",
    "One moment, I'm processing the answer.",
    "Let me think for a second...",
    "Let's see...",
    "I'm evaluating the situation...",
    "I'm analyzing the data...",
    "Please wait a moment while I think...",
    "I need to think about it...",
    "I'm organizing my response...",
    "I'm looking for the best solution...",
    "Give me a second, I'm processing...",
    "One second, I'm thinking about how to respond...",
    "I'm considering the options...",
    "I'm thinking about the best thing to say...",
    "One moment, I'm reviewing the details...",
    "I'm figuring out how to help you best...",
    "I'm evaluating all the factors..."
]

thinking_triggers = [
    # Verbs
    "explain", "describe", "analyze", "calculate", "compare", "evaluate", "solve",
    "write", "create", "find", "list", "suggest", "consider", "identify",
    "define", "demonstrate", "prove", "elaborate", "expand", "summarize",
    "comment", "illustrate", "predict", "classify", "organize", "interpret",


    # Adjectives
    "detailed", "complex", "in-depth", "advanced", "specific", "precise",
    "long", "extensive", "analytical", "complete", "technical", "scientific",

    # Adverbs
    "accurately", "in detail", "completely", "carefully", "meticulously",

    # Common expressions
    "how it works", "what is the difference", "write an example", "explain why",
    "show an example", "find information", "create code", "list all the steps",
    "describe step by step", "how to", "explain in detail", "how to solve",
    "provide explanations", "analyze the situation", "comment on the result",

    # Other deep-analysis verbs
    "investigate", "propose", "simulate", "apply", "optimize",
    "check", "verify", "explore", "model", "explain concepts",

    # Keywords
    "complicated", "difficult", "deep dive", "problem", "solution", "strategy",
    "technique", "procedure", "experiment", "study", "project", "analysis",

    # Question styles
    "what is", "how does it work", "how do you", "what does it mean",
    "what are", "in what way", "why", "for what reason", "in which situations",
    "what does it depend on", "what are the differences", "what are the advantages",
    "what are the disadvantages", "explain the concept", "describe the process",
    "show how", "how is it solved", "how is it calculated",
    "how is it developed", "how is it applied", "how is it built",
    "how is it programmed", "how is it created", "how is it used",
    "how is it implemented", "how is it optimized",

    # Example requests
    "give an example", "show an example", "write an example",
    "explain step by step", "provide detailed explanations",
    "explain how to do it", "explain each step",

    # Long-answer triggers
    "expand on the topic", "analyze in detail", "evaluate carefully",
    "describe accurately", "detail the procedure",
    "provide all details", "develop the answer", "design a plan",
    "create a strategy", "identify all points", "explain with examples",
    "describe the characteristics", "detail the differences",

    # Extended phrasing
    "provide all the information", "explain every detail",
    "describe every phase", "analyze every part",
    "make a complete list", "list all details",
    "explain every aspect", "create a detailed example",
    "describe the entire process", "detail all steps",
    "analyze all options", "explain clearly",
    "provide in-depth explanation", "explain the full procedure"
]

intro_prompt = [{
    "role": "user",
    "content": (
        "You are a personal assistant create by Gabriele Giovinazzo. Introduce yourself in one sentence as a personal assistant in a Jarvis style. "
        "Your creator's name is Gabriele. If you understand that he is the one speaking, "
        "greet him and behave like a friendly assistant."
    )
}]

system_prompt = {
    "role": "system",
    "content": (
        f"You are a virtual assistant named {assistant_name} who speaks English. "
        "When responding, use only continuous text, without titles, subtitles, bullet points, "
        "asterisks, numbers, or special symbols. "
        "The response must be a single, smooth text as if you were speaking aloud."
    )
}
