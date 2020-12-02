from textblob import TextBlob
import pytchat
import time
import threading


messages = []


def timer():
    while True:
        starttime = time.time()
        time.sleep(5 - ((time.time() - starttime) % 5))
        avg = sum(messages)/len(messages)
        if avg > 0:
            avg = str(avg) + " Good"
        elif avg < 0:
            avg = str(avg) + " Bad"
        else:
            avg = str(avg) + " Neutral"
        print(
            "\n\n",
            time.asctime(time.localtime(starttime)),
            " - ",
            time.asctime(time.localtime(time.time())),
            "\n",
            avg,
            "\n\n"
        )
        messages.clear()


if __name__ == "__main__":
    time_thread = threading.Thread(target=timer)
    time_thread.start()

    chat = pytchat.create(video_id="RMZ1a6I86l0")
    while chat.is_alive():
        for c in chat.get().sync_items():
            text = TextBlob(c.message)
            print(f"{round(text.sentiment.polarity, 2)} [{c.author.name}] - {c.message}")
            messages.append(text.sentiment.polarity)
