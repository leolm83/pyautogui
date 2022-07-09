from pynput import mouse

counter=0

def on_click(x, y, button, pressed):
    global counter
   
    if(pressed):
        counter+=1
        print(f"{counter} times {x} {y}")

with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_click=on_click)
listener.start()