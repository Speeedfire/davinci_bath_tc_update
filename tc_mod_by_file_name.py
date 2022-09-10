import sys
import re
from python_get_resolve import GetResolve

def _validate(x):
	# Validate and reformat timecode string

	if len(x) != 11:
		return False

	return x

def reset_clip_timecode():
	projectmanager = resolve.GetProjectManager()
	project        = projectmanager.GetCurrentProject()
	mediapool      = project.GetMediaPool()
	currentbin     = mediapool.GetCurrentFolder()
	clips          = currentbin.GetClips()

	for clip in clips.values():

		name = clip.GetClipProperty('Clip Name')
		pattern = r'\_[0-9]{6}\_'

		time = re.findall(pattern, name)

		if len(time) == 0:
			continue

		fileTime = time[0].replace('_', '')
		rawTime = re.findall(r'[0-9]{2}', fileTime)

		timecode = ":".join(rawTime) + ':00'

		tcValid = _validate(timecode)

		if tcValid:
			print timecode
			# Set new starting timecode to each clip
			clip.SetClipProperty('Start TC', tcValid)

			# Check back new timecodes, pre V17
			print clip.GetClipProperty('Start TC'),\
				clip.GetClipProperty('Clip Name')
		else: 
			continue

if __name__ == '__main__':
	resolve = app.GetResolve()

	reset_clip_timecode()
