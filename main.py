import time
import random
import threading

# Config
import config

# Core
from core.tts import speak_text, speak_async_queue
from core.stt import listen_for_activation, listen_for_command
from core.wakeword import is_wake_word
from core.voice import append_to_log

# AI
from ai.chatgpt import chatgpt_conversation, chatgpt_stream, stream_to_sentences
from ai.memory import add_conversation_memory
from ai.prompts import (
    starting_phrases, continued_phrases,
    thinking_phrases, thinking_triggers,
    intro_prompt, system_prompt
)

# Brain
from brain.commands import handle_voice_command

# Services
from services.events import Events

# Hardware
from hardware.led import led_flash_on_wakeword


# ---------------- STARTUP ----------------

intro_conv = chatgpt_conversation(intro_prompt)
intro_text = intro_conv[-1]["content"]

print(f"🤖 Assistant: {intro_text}\n")
speak_text(intro_text)


# ---------------- CONVERSATION STATE ----------------

interaction_counter = 0
conversation = [system_prompt]


# ---------------- EVENTS ----------------

events = Events()

thread_events = threading.Thread(target=events.check_events, daemon=True)
thread_events.start()


# ---------------- MAIN LOOP ----------------

while True:
    print(f"Say {config.assistant_name} to start...")

    wake_text = listen_for_activation()
    if not wake_text:
        continue

    print("You said:", wake_text)

    if is_wake_word(wake_text):

        interaction_counter += 1
        led_flash_on_wakeword()

        ready_phrase = random.choice(
            starting_phrases if interaction_counter == 1 else continued_phrases
        )

        print(ready_phrase)
        speak_text(ready_phrase)
        time.sleep(0.3)

        user_text = listen_for_command()

        if not user_text:
            print("↩ Command not understood.")
            speak_text("I didn't understand, could you please repeat?")
            led_flash_on_wakeword()

            user_text = listen_for_command()

            if not user_text:
                print("↩ Command still not understood, returning to wake word.")
                continue

        print(f"You said: {user_text}")
        append_to_log(f"You: {user_text}")

        # ---------------- VOICE COMMANDS ----------------
        if handle_voice_command(user_text, events):
            continue

        # ---------------- THINKING TRIGGERS ----------------
        if any(word in user_text.lower() for word in thinking_triggers):
            phrase = random.choice(thinking_phrases)
            speak_async_queue(phrase)

        # ---------------- CHATGPT ----------------
        conversation.append({'role': 'user', 'content': user_text})

        stream = chatgpt_stream(conversation)

        if stream is None:
            conversation = chatgpt_conversation(conversation)
            response_text = conversation[-1]['content']
            speak_async_queue(response_text)

        else:
            full_response = []

            def on_sentence(sentence):
                full_response.append(sentence)
                speak_async_queue(sentence)

            stream_to_sentences(stream, on_sentence)

            final_text = " ".join(full_response)

            conversation.append({
                'role': 'assistant',
                'content': final_text
            })

            append_to_log(f"Assistant: {final_text}")
            add_conversation_memory(user_text, final_text)

        time.sleep(0.2)