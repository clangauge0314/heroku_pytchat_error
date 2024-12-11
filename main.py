import pytchat
import time

ids = ['g5vKkS19nq8', 'kHo37taBFP8', '6IJpVVGIxno', 'LPI_FnuvfhE']

for id in ids:
    try:
        chat = pytchat.create(video_id=id, interruptable=False)
        print(f"Successfully created chat object for video_id: {id}")
        
        #while chat.is_alive():
            #for c in chat.get().items:
                #print(f"[{c.author.name}] {c.message}")
            #time.sleep(1)  

    except Exception as e:
        print(f"Failed to create chat object for video_id: {id}")
        print(f"Error: {e}")
