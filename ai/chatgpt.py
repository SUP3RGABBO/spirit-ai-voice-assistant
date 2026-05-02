import re
import requests
import config
from core.tts import speak_async_queue


def chatgpt_conversation(conversation):
    try:
        response = config.client.chat.completions.create(
            model="gpt-5-mini",
            messages=conversation
        )

        role = response.choices[0].message.role
        content = response.choices[0].message.content

        conversation.append({
            "role": role,
            "content": content
        })

        return conversation

    except requests.exceptions.ConnectionError:
        error_msg = "I am not connected to the Internet. Please check your connection."
        print(error_msg)
        speak_async_queue(error_msg)

        conversation.append({
            "role": "assistant",
            "content": error_msg
        })

        return conversation

    except Exception as e:
        print("OpenAI API Error:", e)

        error_msg = "An internal error occurred."

        conversation.append({
            "role": "assistant",
            "content": error_msg
        })

        speak_async_queue(error_msg)

        return conversation


def chatgpt_stream(conversation):
    try:
        stream = config.client.chat.completions.create(
            model="gpt-5-mini",
            messages=conversation,
            stream=True
        )
        return stream

    except Exception as e:
        print("OpenAI streaming error:", e)
        return None


def stream_to_sentences(stream, on_sentence):
    buffer = ""
    for chunk in stream:
        try:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta
            if not delta or not delta.content:
                continue

            buffer += delta.content

            while True:
                match = re.search(r'([^.?!]{50,}[^.?!]*[.?!])', buffer)
                if match:
                    sentence = match.group(0).strip()
                    on_sentence(sentence)
                    buffer = buffer[len(match.group(0)):]
                else:
                    break

        except Exception as e:
            print("Streaming chunk error:", e)
            continue

    if buffer.strip():
        on_sentence(buffer.strip())