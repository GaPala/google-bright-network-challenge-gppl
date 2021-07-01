"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currentlyPlaying = None
        self.paused = False;
        self.playlists = []


    def video_as_string(self, video):
        string = ""
        string+= str(video.title+ " (" + video.video_id + ")"+ " [")
        for j in range(len(video.tags)):
            string+=(video.tags[j])
            if (j != len(video.tags) - 1):
                string+=(" ")
        string+=("]")
        return string

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
        return num_videos


    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()

        print("Here's a list of all available videos:")
        for video in videos:
            if video!=None:
                print(" "+self.video_as_string(video))


    def play_video(self, video_id):

        if self.currentlyPlaying != None:
            print("Stopping video:", self.currentlyPlaying.title)

        try:
            video = self._video_library.get_video(video_id)
            print("Playing video:", video.title)
            self.currentlyPlaying = video
        except:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if self.currentlyPlaying!=None:
            print("Stopping video", self.currentlyPlaying.title)
            self.currentlyPlaying=None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        video = random.choice(self._video_library.get_all_videos())
        self.play_video(video.video_id)


    def pause_video(self):
        """Pauses the current video."""
        if self.currentlyPlaying == None:
            print("Cannot pause video: No video is currently Playing")
            return

        if self.paused:
            print("Video already paused:", self.currentlyPlaying.title)
        else:
            print("Pausing Video:", self.currentlyPlaying.title)
            self.paused = True


    def continue_video(self):
        """Resumes playing the current video."""
        if self.currentlyPlaying == None:
            print("Cannot continue video: No video is currently Playing")
            return

        if self.paused:
            print("Continuing video:", self.currentlyPlaying.title)
            self.paused=False
        else:
            print("Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""

        try:
            video = self.currentlyPlaying
            print("Currently playing:", self.video_as_string(video) )
        except:
            print("Nothing is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                print("Cannot create playlist: A playlist with the same name already exists")

        # if playlist does not already exist, create it and intialise to empty
        self.playlists.append([playlist_name])
        print("Successfully created new playlist:", playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        #check if video exists
        try:
            self._video_library.get_video(video_id)
        except:
            print("Cannot add video to my_playlist: Video does not exist")
            return

        # search for playlist and add video to it
        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                #check if video already is in playist
                if self.currentlyPlaying in self.playlists[i]:
                    print("Cannot add video to my_PLAYlist: Video already added")
                    return
                else:
                    self.playlists[i].append(self._video_library.get_video(video_id))
                    print("Added video to my_playlist:",self._video_library.get_video(video_id).title)
                    return
        print("Cannot add video to another_playlist: Playlist does not exist")


    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlists) ==0:
            print("No playlists exist yet")
            return

        for i in range(len(self.playlists)):
            print(self.playlists[i][0])


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        # search for playlist
        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                if len(self.playlists[i])==0:
                    print("No videos here yet")
                    return
                else:
                    print("Showing playlist:", self.playlists[i][0])
                    for j in range(1, len(self.playlists[i])):
                        video = self.playlists[i][j]
                        print(" "+self.video_as_string(video))
                    return

        print("Cannot show playlist",playlist_name+": Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        # check if video exists
        try:
            self._video_library.get_video(video_id)
        except:
            print("Cannot remove video from my_playlist: Video does not exist")

        # search for playlist
        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                try:
                    self.playlists[i].remove(self._video_library.get_video(video_id))
                    print("Removed video from",self.playlists[i][0],":",self._video_library.get_video(video_id).title)
                    return
                except:
                    print("Cannot remove video from" ,self.playlists[i][0]+": Video is not in playlist")
                    return
        print("Cannot remove video from",self.playlists[i][0]+": Playlist does not exist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                self.playlists[i] = [ self.playlists[i][0] ]
                print("Successfully removed all videos from", self.playlists[i][0])
                return
        print("Cannot clear playlist ",self.playlists[i][0]+": Playlist does not exist")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for i in range(len(self.playlists)):
            if self.playlists[i][0].lower == playlist_name.lower:
                playlist_name_stored = self.playlists[i][0]
                self.playlists.pop(i)
                print("Deleted playlist:",playlist_name_stored)
                return

        print("Cannot delete playlist my_playlist: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        #videos =

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
