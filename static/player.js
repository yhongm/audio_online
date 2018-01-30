/**
 * Player class containing the state of our playlist and where we are in it.
 * Includes all methods for playing, skipping, updating the display, etc.
 * @param {Array} playlist Array of objects with playlist song details ({title, file, howl}).
 */

var Player = function (playlist) {
    this.playlist = playlist;
    this.index = 0;
    console.log("player,pl.length:" + playlist.length)
    // Display the title of the first track.

    track.innerHTML = '1. ' + playlist[0].title;

    // Setup the playlist display.
    playlist.forEach(function (song) {
        var div = document.createElement('div');
        div.className = 'list-song';
        div.innerHTML = song.title;
        console.log("foreach:" + song.title)
        div.onclick = function () {
            player.skipTo(playlist.indexOf(song));
        };
        list.appendChild(div);
    });
    var setList = function (playlist) {
        this.playlist = playlist;
        this.index = 0;

        // Display the title of the first track.
        // track.innerHTML = '1. ' + playlist[0].title;

        // Setup the playlist display.
        playlist.forEach(function (song) {
            var div = document.createElement('div');
            div.className = 'list-song';
            div.innerHTML = song.title;
            div.onclick = function () {
                player.skipTo(playlist.indexOf(song));
            };
            list.appendChild(div);
        });
    }

};


Player.prototype = {
    /**
     * Play a song in the playlist.
     * @param  {Number} index Index of the song in the playlist (leave empty to play the first or current).
     */


    play: function (index) {
        var self = this;
        var sound;

        index = typeof index === 'number' ? index : self.index;
        var data = self.playlist[index];

        // If we already loaded this track, use the current one.
        // Otherwise, setup and load a new Howl.
        if (data.howl) {
            console.log("have:" + data.howl)
            sound = data.url;
        } else {
            sound = data.howl = new Howl({
                src: data.src,


                html5: true, // Force to HTML5 so that the audio can stream in (best for large files).
                onplay: function () {
                    // Display the duration.
                    duration.innerHTML = self.formatTime(Math.round(sound.duration()));

                    // Start upating the progress of the track.
                    requestAnimationFrame(self.step.bind(self));

                    // Start the wave animation if we have already loaded
                    wave.container.style.display = 'block';
                    bar.style.display = 'none';
                    pauseBtn.style.display = 'block';
                },
                onload: function () {
                    // Start the wave animation.
                    wave.container.style.display = 'block';
                    bar.style.display = 'none';
                    loading.style.display = 'none';
                },
                onend: function () {
                    // Stop the wave animation.
                    wave.container.style.display = 'none';
                    bar.style.display = 'block';
                    self.skip('right');
                },
                onpause: function () {
                    // Stop the wave animation.
                    wave.container.style.display = 'none';
                    bar.style.display = 'block';
                },
                onstop: function () {
                    // Stop the wave animation.
                    wave.container.style.display = 'none';
                    bar.style.display = 'block';
                }
            });
        }

        // Begin playing the sound.
        sound.play();

        // Update the track display.
        track.innerHTML = (index + 1) + '. ' + data.title;

        // Show the pause button.
        if (sound.state() === 'loaded') {
            playBtn.style.display = 'none';
            pauseBtn.style.display = 'block';
        } else {
            loading.style.display = 'block';
            playBtn.style.display = 'none';
            pauseBtn.style.display = 'none';
        }

        // Keep track of the index we are currently playing.
        self.index = index;
    },

    /**
     * Pause the currently playing track.
     */
    pause: function () {
        var self = this;

        // Get the Howl we want to manipulate.
        var sound = self.playlist[self.index].howl;

        // Puase the sound.
        sound.pause();

        // Show the play button.
        playBtn.style.display = 'block';
        pauseBtn.style.display = 'none';
    },

    /**
     * Skip to the next or previous track.
     * @param  {String} direction 'next' or 'prev'.
     */
    skip: function (direction) {
        var self = this;

        // Get the next track based on the direction of the track.
        var index = 0;
        if (direction === 'prev') {
            index = self.index - 1;
            if (index < 0) {
                index = self.playlist.length - 1;
            }
        } else {
            index = self.index + 1;
            if (index >= self.playlist.length) {
                index = 0;
            }
        }

        self.skipTo(index);
    },

    /**
     * Skip to a specific track based on its playlist index.
     * @param  {Number} index Index in the playlist.
     */
    skipTo: function (index) {
        var self = this;

        // Stop the current track.
        if (self.playlist[self.index].howl) {
            self.playlist[self.index].howl.stop();
        }

        // Reset progress.
        progress.style.width = '0%';

        // Play the new track.
        self.play(index);
    },

    /**
     * Set the volume and update the volume slider display.
     * @param  {Number} val Volume between 0 and 1.
     */
    volume: function (val) {
        var self = this;

        // Update the global volume (affecting all Howls).
        Howler.volume(val);

        // Update the display on the slider.
        var barWidth = (val * 90) / 100;
        barFull.style.width = (barWidth * 100) + '%';
        sliderBtn.style.left = (window.innerWidth * barWidth + window.innerWidth * 0.05 - 25) + 'px';
    },

    /**
     * Seek to a new position in the currently playing track.
     * @param  {Number} per Percentage through the song to skip.
     */
    seek: function (per) {
        var self = this;

        // Get the Howl we want to manipulate.
        var sound = self.playlist[self.index].howl;

        // Convert the percent into a seek position.
        if (sound.playing()) {
            sound.seek(sound.duration() * per);
        }
    },

    /**
     * The step called within requestAnimationFrame to update the playback position.
     */
    step: function () {
        var self = this;

        // Get the Howl we want to manipulate.
        var sound = self.playlist[self.index].howl;

        // Determine our current seek position.
        var seek = sound.seek() || 0;
        timer.innerHTML = self.formatTime(Math.round(seek));
        progress.style.width = (((seek / sound.duration()) * 100) || 0) + '%';

        // If the sound is still playing, continue stepping.
        if (sound.playing()) {
            requestAnimationFrame(self.step.bind(self));
        }
    },

    /**
     * Toggle the playlist display on/off.
     */
    togglePlaylist: function () {
        var self = this;
        var display = (playlist.style.display === 'block') ? 'none' : 'block';

        setTimeout(function () {
            playlist.style.display = display;
        }, (display === 'block') ? 0 : 500);
        playlist.className = (display === 'block') ? 'fadein' : 'fadeout';
    },

    /**
     * Toggle the volume display on/off.
     */
    toggleVolume: function () {
        var self = this;
        var display = (volume.style.display === 'block') ? 'none' : 'block';

        setTimeout(function () {
            volume.style.display = display;
        }, (display === 'block') ? 0 : 500);
        volume.className = (display === 'block') ? 'fadein' : 'fadeout';
    },

    /**
     * Format the time from seconds to M:SS.
     * @param  {Number} secs Seconds to format.
     * @return {String}      Formatted time.
     */
    formatTime: function (secs) {
        var minutes = Math.floor(secs / 60) || 0;
        var seconds = (secs - minutes * 60) || 0;

        return minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
    }
};



