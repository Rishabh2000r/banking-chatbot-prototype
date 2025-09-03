from gui import demo
from api import app

import threading

if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False), daemon=True).start()
    
    demo.launch()