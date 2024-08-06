import json
import time
from websocket import create_connection
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, ws):
        self.ws = ws
        self.last_sent_data = None

    def on_modified(self, event):
        if event.src_path.endswith(machine_file):
            try:
                with open(machine_file, 'r') as f:
                    data = json.load(f)
                if data != self.last_sent_data:
                    self.ws.send(json.dumps(data))
                    self.last_sent_data = data
                    print("Data sent to server:", data)
            except json.JSONDecodeError:
                print("Error: JSON file is empty or invalid")

def start_agent():
    print("Connecting to WebSocket server...")
    ws = create_connection('ws://localhost:8000/ws/machine/M2/')
    print("Connected to WebSocket server")

    observer = Observer()
    event_handler = FileChangeHandler(ws)
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    
    try:
        while True:
            try:
                result = ws.recv()
                if result:
                    try:
                        data = json.loads(result)
                        with open(machine_file, 'w') as f:
                            json.dump(data, f, indent=4)
                        print("Data received from server:", result)
                    except json.JSONDecodeError:
                        print("Error: Received invalid JSON")
            except Exception as e:
                print(f"Error receiving data from WebSocket: {e}")
            time.sleep(0.1)  # Reduced sleep time to make the loop more responsive
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()
        ws.close()
        print("Disconnected from WebSocket server")

if __name__ == "__main__":
    machine_file = 'machine2.json'
    start_agent()
