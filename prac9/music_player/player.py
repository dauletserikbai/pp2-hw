import pygame
import os 

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init() 
        self.music_folder = music_folder 
        self.playlist = self.load_tracks() 
        self.current_index = 0 
        self.status = "Stopped" 
        self.track_length = 1 

    def load_tracks(self): 
        tracks = []
        for file in os.listdir(self.music_folder): 
            if file.endswith(".mp3") or file.endswith(".wav"):
                tracks.append(os.path.join(self.music_folder, file)) 
                
        tracks.sort()
        return tracks

    def play(self):
        if not self.playlist:
            return 
        track = self.playlist[self.current_index] 
        pygame.mixer.music.load(track) 
        pygame.mixer.music.play()
        self.status = "Playing"
        
        try:
            sound = pygame.mixer.Sound(track)
            self.track_length = sound.get_length()
        except:
            self.track_length = 1

    def stop(self):
        pygame.mixer.music.stop()
        self.status = "Stopped"

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist) 
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist) 
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks"
        return os.path.basename(self.playlist[self.current_index])

    def get_progress(self):
        if self.status != "Playing":
            return 0
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms < 0:
            return 0
        return min(pos_ms / (self.track_length * 1000), 1)