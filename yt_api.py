from pyyoutube import Client


# https://github.com/youtube/api-samples/tree/master/python FAJNY LINK
# https://skillshats.com/blogs/how-to-use-the-youtube-api-with-python-a-step-by-step-guide/ TO TEZ CIEKAWY LINK















SCOPE = [
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/userinfo.profile",
]
# # authorize_url, state = client.get_authorize_url(scope=SCOPE)

# def do_authorize(client_id: str, client_secret: str):
#     # https://github.com/sns-sdks/python-youtube/blob/master/examples/apis/oauth_flow.py to ten przyklad
#     # https://github.com/sns-sdks/python-youtube/blob/master/docs/docs/authorization.md i ten
#     print(client_id)
#     print(client_secret)
#     client = Client(client_id=client_id, client_secret=client_secret)
#     authorize_url, state = client.get_authorize_url(scope=SCOPE)
#     print(f"Click url to do authorize: {authorize_url}")

#     response_uri = input("Input youtube redirect uri:\n") # copy and paste the redirected url

#     client.generate_access_token(authorization_response=response_uri)

#     return client


REDIRECT_URI = "https://localhost/"

def do_authorize(client_id: str, client_secret: str):
    cli = Client(client_id=client_id, client_secret=client_id)
    # or if you want to use a web type client_secret.json
    # cli = Client(client_secret_path=CLIENT_SECRET_PATH)

    authorize_url, state = cli.get_authorize_url(scope=SCOPE, redirect_uri=REDIRECT_URI)
    print(f"Click url to authorize: {authorize_url}")

    # Manually input the redirected URL from the browser
    response_uri = input("Input YouTube redirect URI:\n")

    token = cli.generate_access_token(authorization_response=response_uri, scope=SCOPE)
    print(f"Your token: {token}")

    # Get data
    resp = cli.channels.list(mine=True)
    print(f"Your channel id: {resp.items[0].id}")












def download_playlist(client: Client, channel_id: str):
    response = client.playlists.list(playlist_id="PLOspHqNVtKAC-_ZAGresP-i0okHe5FjcJ", parts="snippet,contentDetails,status")
    title = response.items[0].snippet.title

# https://github.com/sns-sdks/python-youtube/issues/87 # jesli kod wyzej nie zadziala
# https://github.com/sns-sdks/python-youtube/issues/121

    # response = client.channel.list(mine=True)
    # print(f"Your channel id: {response.items[0].id}")


#to druga wersja
    # resp = cli.channels.list(
    #     channel_id=channel_id, parts=["id", "snippet", "statistics"], return_json=True
    # )
    # print(f"Channel info: {resp['items'][0]}")

    print("I show playlist")


def delete_song(client: Client, video_id):
    client.playlists.delete(video_id=video_id) # podobno playlists jest tak samo jak videos, mimo ze nie ma w dokumentacji
    print("I delete video")