import helpers
import yt_api
import spotify_api

def main():
    yt_client_id, yt_client_secret, channel_id, spotify_client_id, spotify_client_secret, spotify_playlist = helpers.readArgs()

    # client = yt_auth.do_authorize(yt_client_id, yt_client_secret) 
    # this may not work now, because it takes time to change redirect uri in google console
    # yt_auth.download_playlist(client, channel_id)

    names_list = ["justin bieber"] #here should be list from yt

    sp = spotify_api.do_authorize(spotify_client_id, spotify_client_secret)

    for song_name in names_list: #I will have to somehow get idx
        print(song_name)
        tracks = spotify_api.list_songs_by_name(sp, song_name)
        index = helpers.get_integer_input("Enter your name by number listed, or type 10 to skip ")
        if index != 10:
            spotify_api.add_song_to_playlist(sp, tracks[int(index)]['id'], spotify_playlist)
            # yt_api.delete_song()




if __name__ == "__main__": 
    main()