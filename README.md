# Problem Statement 

Data scientists code up a lot of pipelines that can often take a long time due to long pre-processing sequences or massive
amounts of time required. And if errors occur, then the pipeline needs to be re-run. This means we usually want to be notified
as early as possible if errors occurred.

# So what is pipelinenotifier?

Pipeline notifier will send messages to your Slack/Discord/Keybase channel once you set up a webhook. Support can be added for 
more channels if desired. Feel free to ping me at jacky.wong@vctr.ai. It will send error messages so you can tell what is wrong
the moment it happens.

# Data Science Bots

As data scientists, you are running a lot of code over a large amount of time. This often means that that you want to be notified about things via mobile while you have applications running in the background. 

I ended up re-writing this code across a number of organisations.

```
from pipelinenotifier import KeyBaseNotifier

with KeyBaseBot(, "<webhook_url>") as bot:
    # Insert training loop/reader here.
    score = 0.5
    bot.send_message(f"Scored {score}.")

```

If there is an error, it will send the error message to your channel.
