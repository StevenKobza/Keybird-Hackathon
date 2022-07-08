import os
import soundfile as sf
import librosa
import numpy as np
import ntpath
import matplotlib.pyplot as plt
# from librosa import display
import librosa.display

### UTIL FN
def path_leaf(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

### 

def get_onsets(y, sr): # need rewrite
	onset_env = librosa.onset.onset_strength(y, sr=sr,
		aggregate=np.median)

	return onset_env

# useless fn, remove
def get_beats(y, sr, onset_env):
	tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,
		sr=sr)

	return beats

def get_signal_window_by_onsets(current_onset, next_onset):
	pass

### rewrite below ###

def get_sample_sounds_from_onsets(signal, sr, onset_env, audio_db, rec_name, \
		min_vel_treshold=0.25, sample_duration_frames=4096):
	# check if the folder exists
	frame_size = len(signal) / len(onset_env)

	persistence_path = 'data\\reprocessed_{}\\samples_from_onsets\\{}'.format(audio_db, rec_name) #, stem_type)
	os.makedirs(persistence_path, mode=0o777, exist_ok=True)

	audio_samples = []
	# for i in range(len(onset_env):
	skip_frames = 0
	for i in range(len(onset_env)):
		if skip_frames != 0:
			skip_frames = skip_frames - 1
			# print(skip_frames)
			continue

		if onset_env[i] > min_vel_treshold:
			sample_begin = int(i * frame_size)
			audio_samples.append((str(sample_begin), signal[sample_begin:sample_begin+sample_duration_frames]))
			skip_frames = int(sample_duration_frames / frame_size)

	# persist
	for onset_i, sig_val in audio_samples:
		persist_file_path = '{}\\{}.wav'.format(persistence_path, onset_i)
		if os.path.isfile(persist_file_path):
			print('file already exists, skipping . . .')
			continue
		sf.write(persist_file_path, sig_val, sr, 'PCM_24')

	print(rec_name + " - - - done")

	return audio_samples

def visualize_this_stuff(signal, sr, onset_env, beats):
	hop_length = 512
	fig, ax = plt.subplots(nrows=2, sharex=True)
	# M = librosa.feature.melspectrogram(y=signal, sr=sr, hop_length=hop_length)
	# librosa.display.specshow(librosa.power_to_db(M, ref=np.max),
	# 						y_axis='mel', x_axis='time', hop_length=hop_length,
	# 						ax=ax[0])
	# # ax[0].label_outer()
	# ax[0].set(title='Mel spectrogram')
	
	librosa.display.waveplot(y, sr=sr, ax=ax[0])
	ax[0].label_outer()
	ax[0].set(title='Audio Signal')


	times = librosa.times_like(onset_env, sr=sr, hop_length=hop_length)
	ax[1].plot(times, librosa.util.normalize(onset_env),
			label='Onset strength')
	# ax[1].vlines(times[beats], 0, 1, alpha=0.5, color='r',
			# linestyle='--', label='Beats')
	ax[1].legend()

	plt.show()


AUDIO_DB = 'filled types'
kb_rec_dir = 'datasets\\{}'.format(AUDIO_DB)


if __name__ == "__main__":
	for _, (dirpath, _, filenames) in enumerate(os.walk(kb_rec_dir)):
		for f in filenames:
			# recording_name = path_leaf(f)
			recording_name = os.path.splitext(f)[0]
			# os.path.splitext(f)[0]
			print(recording_name)

			recording_file_path = kb_rec_dir + "\\" + f
			print("processing {}".format(recording_file_path))

			y, sr = librosa.load(recording_file_path)

			onsets = get_onsets(y, sr)
			# visualize_this_stuff(y, sr, onsets, get_beats(y,sr,onsets))

			get_sample_sounds_from_onsets(y, sr, onsets, AUDIO_DB, recording_name)
