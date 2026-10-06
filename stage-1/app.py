from __future__ import annotations
import json, os, re, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

STATE = {"fixture": {}, "users": {}, "by_email": {}, "tokens": {}, "payments": {}}

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *args): pass

    def send_json(self, status: int, payload) -> None:
        body = b"" if payload is None else json.dumps(payload).encode()
        self.send_response(status)
        if body: self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body: self.wfile.write(body)

    def fail(self, status: int, code: str) -> None:
        self.send_json(status, {"error":{"code":code,"message":code}})

    def body(self) -> dict|None:
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        if not raw: return {}
        try:
            parsed = json.loads(raw)
            return parsed if isinstance(parsed, dict) else None
        except ValueError: return None

    def do_GET(self): self.route("GET")
    def do_POST(self): self.route("POST")

    def route(self, method: str) -> None:
        path = urlparse(self.path).path.rstrip("/") or "/"

        if method=="GET" and path=="/health":
            return self.send_json(200, {"status":"ok"})

        if method=="POST" and path=="/_test/reset":
            fixture = self.body()
            if fixture is None: return self.fail(400,"malformed_request")
            STATE.update({"fixture":fixture,"users":{}, "by_email":{}, "tokens":{}, "payments":{}})
            for u in fixture.get("users",[]):
                STATE["users"][u["id"]] = u
                STATE["by_email"][u["email"].lower()] = u
            return self.send_json(204,None)

        if method=="POST" and path=="/auth/signup": return self.signup()
        if method=="POST" and path=="/auth/login": return self.login()
        if method=="GET" and path=="/me": return self.me()
        if method=="POST" and path=="/payments": return self.pay()

        return self.fail(501,"not_implemented")

    def signup(self):
        data=self.body()
        if data is None: return self.fail(400,"malformed_request")
        email,password=data.get("email"),data.get("password")
        if not isinstance(email,str) or not isinstance(password,str):
            return self.fail(400,"malformed_request")
        if email.lower() in STATE["by_email"]: return self.fail(409,"email_taken")
        user={"id":f"u_{uuid.uuid4().hex[:8]}","email":email,"password":password,
              "display_name":data.get("display_name"),"handle":email.split("@")[0][:20],"balance":0}
        STATE["users"][user["id"]]=user; STATE["by_email"][email.lower()]=user
        token=uuid.uuid4().hex; STATE["tokens"][token]=user["id"]
        return self.send_json(201,{"user_id":user["id"],"display_name":user["display_name"],"token":token})

    def login(self):
        data=self.body()
        if data is None: return self.fail(400,"malformed_request")
        user=STATE["by_email"].get(str(data.get("email","")).lower())
        if user is None or data.get("password")!=user["password"]:
            return self.fail(401,"unauthenticated")
        token=uuid.uuid4().hex; STATE["tokens"][token]=user["id"]
        return self.send_json(200,{"user_id":user["id"],"display_name":user["display_name"],"token":token})

    def me(self):
        auth=self.headers.get("Authorization","").replace("Bearer ","")
        uid=STATE["tokens"].get(auth)
        if not uid: return self.fail(401,"unauthenticated")
        u=STATE["users"][uid]
        return self.send_json(200,{"user_id":u["id"],"handle":u["handle"],"balance":u["balance"]})

    def pay(self):
        data=self.body()
        if data is None: return self.fail(400,"malformed_request")
        auth=self.headers.get("Authorization","").replace("Bearer ","")
        uid=STATE["tokens"].get(auth)
        if not uid: return self.fail(401,"unauthenticated")
        sender=STATE["users"][uid]
        to_handle=data.get("to_handle"); amount=data.get("amount"); note=data.get("note","")
        if not isinstance(amount,int) or amount<=0 or amount>1_000_000_000:
            return self.fail(422,"validation_failed")
        if not isinstance(to_handle,str) or not re.fullmatch(r"[a-z0-9_]{1,20}",to_handle):
            return self.fail(422,"validation_failed")
        recipient=None
        for u in STATE["users"].values():
            if u["handle"]==to_handle: recipient=u
        if recipient is None: return self.fail(404,"not_found")
        if len(note)>200: return self.fail(422,"validation_failed")
        if sender["balance"]<amount: return self.fail(409,"insufficient_funds")
        sender["balance"]-=amount; recipient["balance"]+=amount
        pid=uuid.uuid4().hex
        payment={"payment_id":pid,"from_handle":sender["handle"],"to_handle":recipient["handle"],
                 "amount":amount,"note":note}
        STATE["payments"][pid]=payment
        return self.send_json(201,payment)

class Server(ThreadingHTTPServer):
    request_queue_size=256; daemon_threads=True

def main():
    port=int(os.environ.get("PORT","8080"))
    print(f"listening on 0.0.0.0:{port}",flush=True)
    Server(("0.0.0.0",port),Handler).serve_forever()

if __name__=="__main__": main()
