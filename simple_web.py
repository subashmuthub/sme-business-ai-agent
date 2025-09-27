import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from agent import SMEBusinessAgent
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
from urllib.parse import parse_qs
import webbrowser

class SMEHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>SME Business AI Agent</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .chat-box { border: 1px solid #ccc; height: 400px; overflow-y: scroll; padding: 10px; margin: 20px 0; }
                    .user { color: blue; font-weight: bold; }
                    .ai { color: green; font-weight: bold; }
                    input[type="text"] { width: 70%; padding: 10px; }
                    button { padding: 10px 20px; background: #007cba; color: white; border: none; cursor: pointer; }
                </style>
            </head>
            <body>
                <h1>🏢 SME Business AI Agent</h1>
                <div class="chat-box" id="chatBox"></div>
                <input type="text" id="userInput" placeholder="Ask about your business..." onkeypress="handleEnter(event)">
                <button onclick="sendMessage()">Send</button>
                
                <h3>Quick Questions:</h3>
                <button onclick="askQuestion('What was the profit in May 2023?')">May Profit</button>
                <button onclick="askQuestion('Summarize Q1 2023 performance')">Q1 Summary</button>
                <button onclick="askQuestion('Suggest improvements for June')">June Tips</button>
                
                <script>
                    function sendMessage() {
                        const input = document.getElementById('userInput');
                        const question = input.value;
                        if (!question) return;
                        
                        addToChat('You: ' + question, 'user');
                        input.value = '';
                        
                        fetch('/ask?q=' + encodeURIComponent(question))
                            .then(response => response.text())
                            .then(answer => addToChat('AI: ' + answer, 'ai'));
                    }
                    
                    function askQuestion(q) {
                        document.getElementById('userInput').value = q;
                        sendMessage();
                    }
                    
                    function addToChat(message, className) {
                        const chatBox = document.getElementById('chatBox');
                        const div = document.createElement('div');
                        div.className = className;
                        div.textContent = message;
                        chatBox.appendChild(div);
                        chatBox.scrollTop = chatBox.scrollHeight;
                    }
                    
                    function handleEnter(event) {
                        if (event.key === 'Enter') sendMessage();
                    }
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        
        elif self.path.startswith('/ask'):
            query = parse_qs(self.path.split('?')[1])['q'][0]
            agent = SMEBusinessAgent()
            response = agent.simple_query(query)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode())

def run_simple_server():
    server = HTTPServer(('localhost', 8000), SMEHandler)
    print("🚀 Starting SME Business AI Agent at http://localhost:8000")
    webbrowser.open('http://localhost:8000')
    server.serve_forever()

if __name__ == "__main__":
    run_simple_server()