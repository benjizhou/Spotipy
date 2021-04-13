import sys

import spotipy
import spotipy.util as util
 
scope = 'user-read-currently-playing'
username = 'benjizhou'
token = util.prompt_for_user_token(username, scope)

spotify = spotipy.Spotify(auth=token)

def run():
    current_track = spotify.current_user_playing_track()
    return(current_track['item']['name'] + ' // ' + current_track['item']['artists'][0]['name'])

def name():
    current_track = spotify.current_user_playing_track()
    return(current_track['item']['name'])

def artist():
    current_track = spotify.current_user_playing_track()
    return(current_track['item']['artists'][0]['name'])

def playing():
    return(spotify.current_user_playing_track())

def features(track):
    return(spotify.audio_analysis('spotify:track:4TTV7EcfroSLWzXRY6gLv6'))

def id():
    return(spotify.id)

# def genre():
#     return(spotify.audio_analysis(spotify.current_user_playing_track()['item']['uri']))

def rec():
    return (spotify.artist_related_artists(spotify.current_user_playing_track()['item']['artists'][0]['uri'])['item']['genres'])
# def played():
#     return(spotify.current_user_recently_played(limit=1, after=None, before=None)['items'][0])