import re

class WAF:
    def __init__(self):
        self.rules = [
            # Rule 1: Block SQL injection attacks
            {"pattern": r"SELECT|INSERT|UPDATE|DELETE", "action": "block"},
            # Rule 2: Block cross-site scripting (XSS) attacks
            {"pattern": r"<script|<img|<a", "action": "block"},
            # Rule 3: Block remote file inclusion (RFI) attacks
            {"pattern": r"http://|https://", "action": "block"},
            # Rule 4: Block PHP code execution
            {"pattern": r"<?php|<?|?>", "action": "block"}
        ]

    def inspect_request(self, request):
        for rule in self.rules:
            if re.search(rule["pattern"], request):
                return False
        return True

    def inspect_response(self, response):
        for rule in self.rules:
            if re.search(rule["pattern"], response):
                return False
        return True

def main():
    waf = WAF()

    # Example request and response
    request = "GET /index.php?username=admin&password=123 HTTP/1.1"
    response = "<html><body>Welcome, admin!</body></html>"

    if waf.inspect_request(request):
        print("Request allowed")
    else:
        print("Request blocked")

    if waf.inspect_response(response):
        print("Response allowed")
    else:
        print("Response blocked")

if __name__ == "__main__":
    main()