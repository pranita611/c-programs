import http.server
import socketserver
import json
import subprocess
import os
from socketserver import ThreadingMixIn

PORT = 8080

class ThreadedTCPServer(ThreadingMixIn, socketserver.TCPServer):
    pass

class SimHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/run_sim':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse the input string sent from the frontend
                data = json.loads(post_data)
                sim_input = data.get('input', '')

                # Run the C executable and pipe the input string to it
                sim_process = subprocess.Popen(['./traffic_engine.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                # Send the input to the C program
                stdout, stderr = sim_process.communicate(input=sim_input)

                # The C program generated simulation.json. Read it and send it to the frontend.
                if os.path.exists('simulation.json'):
                    with open('simulation.json', 'r') as f:
                        sim_data = json.load(f)
                        
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(sim_data).encode())
                else:
                    self.send_response(500)
                    self.end_headers()
                    self.wfile.write(b'{"error": "simulation.json was not generated. C program might have crashed. Check your input format."}')
                    
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    print(f"Starting multi-threaded server at http://localhost:{PORT}")
    # Use ThreadedTCPServer for better performance
    with ThreadedTCPServer(("0.0.0.0", PORT), SimHandler) as httpd:
        httpd.serve_forever()
