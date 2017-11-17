
class Animation:
	def animateFrame(self, speed, instant, tracking, size):
		nextInstant = list(instant)
		
		#recursion termination check
		if self.validation(tracking[len(tracking)-1]): return tracking
		
		i = 0
		for p in instant:			
			for char in p:	
				if char == "L" and i >= speed:													
					nextInstant[i-speed] += char
					
				elif char == "R" and i < (size-speed):													
					nextInstant[i+speed] += char
				
				nextInstant[i] = nextInstant[i][1:]
							
			if nextInstant[i] == "": nextInstant[i] = "."			
				
			i += 1			
		
		tracking.append(self.transcribeTrack(nextInstant))
		
		return self.animateFrame(speed, nextInstant, tracking, size)				
		
	def transcribeTrack(self, instant):
		track = ""
		for x in instant:
			if x == "." or x == "": track += "."
			else: track += "X"
		return track
	
	#terminate recursion if no 'X' in chamber
	def validation(self, track):
		for s in track:
			if s == "X": return False
		return True
		
	def animate(self, speed, initPos):								
		if speed < 1: return "error"
		tracking = list()
		instant = list(initPos)
		
		tracking.append(self.transcribeTrack(instant))
		size = len(initPos)
		return self.animateFrame(speed, instant, tracking, size)
