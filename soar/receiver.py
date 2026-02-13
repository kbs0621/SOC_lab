from fastapi import FastAPI
import os
import subprocess

app = FastAPI()

@app.post("/soar/block")
def block_ip(ip: str):
    try:
        subprocess.run(["ufw", "deny", "from", ip], check=True)
        return {"status": "blocked", "ip": ip}
    except Exception as e:
        return {"error": str(e)}
