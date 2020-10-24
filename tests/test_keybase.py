from pipelinenotifier import *
import os

def test_discord():
    with DiscordNotifier(project_name="test_project", webhook_url=os.environ['DISCORD_URL'], username="test_username") as bot:
        bot.send_message("Testing Discord notifications.")

def test_slack():
    with SlackNotifier(project_name='test_project', webhook_url=os.environ['SLACK_URL'], username='test_username') as bot:
        bot.send_message("Testing Slack notifications.")

def test_keybase():
    with KeyBaseNotifier(project_name='test_project', webhook_url=os.environ['WEBHOOK_URL']) as bot:
        bot.send_message("Testing Keybase notifications.")
