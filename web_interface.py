import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from sme_business_agent import SimpleBusinessAgent
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
                    body { 
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                        max-width: 1000px; 
                        margin: 0 auto; 
                        padding: 20px;
                        background: #f8f9fa;
                        color: #333;
                    }
                    .header {
                        background: linear-gradient(135deg, #2d5aa0 0%, #1f4e79 100%);
                        color: white;
                        padding: 2rem;
                        border-radius: 10px;
                        text-align: center;
                        margin-bottom: 2rem;
                    }
                    .chat-box { 
                        border: 1px solid #ddd; 
                        height: 400px; 
                        overflow-y: auto; 
                        padding: 15px; 
                        margin: 20px 0;
                        background: white;
                        border-radius: 8px;
                    }
                    .user { color: #2d5aa0; font-weight: bold; margin: 10px 0; }
                    .ai { color: #28a745; font-weight: bold; margin: 10px 0; }
                    .input-group { display: flex; gap: 10px; margin: 20px 0; }
                    .chat-input { 
                        flex: 1; 
                        padding: 12px; 
                        border: 2px solid #ddd;
                        border-radius: 6px;
                        font-size: 16px;
                    }
                    .send-btn { 
                        padding: 12px 24px; 
                        background: #2d5aa0; 
                        color: white; 
                        border: none; 
                        cursor: pointer;
                        border-radius: 6px;
                        font-weight: 600;
                    }
                    .send-btn:hover { background: #1f4e79; }
                    .quick-actions { 
                        display: grid; 
                        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                        gap: 10px; 
                        margin: 20px 0; 
                    }
                    .quick-btn {
                        background: #28a745;
                        border: none;
                        padding: 15px;
                        border-radius: 6px;
                        color: white;
                        cursor: pointer;
                        font-weight: 500;
                    }
                    .quick-btn:hover { background: #218838; }
                    .footer {
                        text-align: center;
                        padding: 20px;
                        color: #6c757d;
                        border-top: 1px solid #ddd;
                        margin-top: 2rem;
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>🤖 SME Business AI Agent</h1>
                    <p>Intelligent Business Analytics Platform</p>
                </div>
                
                <div class="chat-box" id="chatBox">
                    <div class="ai">🤖 AI Assistant: Hello! I'm ready to help analyze your business data. Ask me about profits, sales trends, or recommendations.</div>
                </div>
                
                <div class="input-group">
                    <input type="text" class="chat-input" id="userInput" placeholder="Ask about your business performance..." onkeypress="handleEnter(event)">
                    <button class="send-btn" onclick="sendMessage()">Send</button>
                </div>
                
                <h3>Quick Questions:</h3>
                <div class="quick-actions">
                    <button class="quick-btn" onclick="askQuestion('What was the profit in May 2023?')">May Profit</button>
                    <button class="quick-btn" onclick="askQuestion('Summarize Q1 2023 performance')">Q1 Summary</button>
                    <button class="quick-btn" onclick="askQuestion('Suggest improvements for June')">Recommendations</button>
                    <button class="quick-btn" onclick="askQuestion('Which month had highest sales?')">Top Sales Month</button>
                </div>
                
                <div class="footer">
                    🤖 SME Business AI Agent | Powered by Advanced AI
                </div>
                
                <script>
                    function sendMessage() {
                        const input = document.getElementById('userInput');
                        const question = input.value.trim();
                        if (!question) return;
                        
                        addToChat('You: ' + question, 'user');
                        input.value = '';
                        
                        const loadingDiv = addToChat('🤖 AI Assistant: Analyzing your request...', 'ai');
                        
                        fetch('/ask?q=' + encodeURIComponent(question))
                            .then(response => response.text())
                            .then(answer => {
                                loadingDiv.innerHTML = '<strong>🤖 AI Assistant:</strong> ' + answer;
                            })
                            .catch(error => {
                                loadingDiv.innerHTML = '<strong>🤖 AI Assistant:</strong> Sorry, there was an error processing your request.';
                            });
                    }
                    
                    function askQuestion(q) {
                        document.getElementById('userInput').value = q;
                        sendMessage();
                    }
                    
                    function addToChat(message, className) {
                        const chatBox = document.getElementById('chatBox');
                        const div = document.createElement('div');
                        div.className = className;
                        div.innerHTML = message;
                        chatBox.appendChild(div);
                        chatBox.scrollTop = chatBox.scrollHeight;
                        return div;
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
            agent = SimpleBusinessAgent()
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