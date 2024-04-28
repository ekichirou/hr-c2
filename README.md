# HighRise C2
This is a small project based on the famous crypto game [HighRise](https://highrise.game)</br>
This project is being coded in python, using HR web api and Discord's webhook for unauth payload delivery.
<hr>
How it works:</br>
&middot; Step 1: Create a <b>TEXT</b> post in HR.</br>
&middot; Step 2: Navigate to <a href="https://highrise.game">https://highrise.game</a> and click on your Profile at the top right corner. Once you have done that click on your post created from within the game, this will show you the <code>post_id</code> in the address bar as show in the picture bellow:</br>
![image](https://github.com/ekichirou/hr-c2/assets/9247107/25ef729b-3039-4c8e-a00e-d02e145f8449)</br>
&middot; Step 3: Create a Discord [webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) within your text channel. This is where the output of the command in the HR post will be sent to.</br>
&middot; Step 4: Supply both <code>post_id</code> and the webhook url in the python script.
<hr>
- <code>hr_post_url</code> is for the <code>post_id</code></br>
- <code>dc_webhook_url</code> is for the Discord webhook url</br>
Short demo in here: <a href="https://youtu.be/VfU3IVVuoPA">https://youtu.be/VfU3IVVuoPA</a>
