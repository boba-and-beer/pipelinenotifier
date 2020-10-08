# Data Science Bots

As data scientists, you are running a lot of code over a large amount of time. This often means that that you want to be notified about things via mobile while you have applications running in the background. 

I ended up re-writing this code across a number of organisations.

```
from jackywong import KeyBaseBot

with KeyBaseBot("project_name | Jacky Wong", "<webhook_url>") as bot:
    score = 0.5
    bot.send_message(f"Scored {score}.")


```

# FAQ

Why did you name the repository after yourself? 
Not sure. Let me know if there's a better one.
