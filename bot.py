from slackclient import SlackClient
import config

slack_token = config.token
sc = SlackClient(slack_token)

if __name__ == "__main__":
    sc.api_call(
        "chat.postMessage",
        channel="CG263QPBK",
        text="Hello from Python! :tada:"
    )
