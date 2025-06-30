import pyttsx3
import threading
import time

class AudioGenerator:
    def __init__(self, voice_rate=150, voice_volume=0.9):
        """
        Initialize the audio generator
        
        Args:
            voice_rate (int): Speech rate (words per minute)
            voice_volume (float): Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_rate)
        self.engine.setProperty('volume', voice_volume)
        
        # Get available voices and set to first available
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        
        self.is_speaking = False
        self.speech_queue = []
        self.speech_thread = None
        
    def speak(self, text, block=False):
        """
        Speak the given text
        
        Args:
            text (str): Text to speak
            block (bool): If True, wait for speech to complete
        """
        if not text or not text.strip():
            return
            
        if block:
            # Blocking speech - wait for completion
            self._speak_text(text)
        else:
            # Non-blocking speech - add to queue
            self.speech_queue.append(text)
            if not self.is_speaking:
                self._start_speech_thread()
    
    def _speak_text(self, text):
        """Internal method to speak text"""
        try:
            self.is_speaking = True
            print(f"🔊 Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speech: {e}")
        finally:
            self.is_speaking = False
    
    def _start_speech_thread(self):
        """Start the speech thread to process queue"""
        if self.speech_thread and self.speech_thread.is_alive():
            return
            
        self.speech_thread = threading.Thread(target=self._process_speech_queue)
        self.speech_thread.daemon = True
        self.speech_thread.start()
    
    def _process_speech_queue(self):
        """Process the speech queue"""
        while self.speech_queue:
            if not self.is_speaking:
                text = self.speech_queue.pop(0)
                self._speak_text(text)
            else:
                time.sleep(0.1)
    
    def speak_opcua_value(self, tag_name, value, tag_type="Tag"):
        """
        Speak OPC-UA tag value in a natural way
        
        Args:
            tag_name (str): Name of the tag
            value: Value of the tag
            tag_type (str): Type of tag (VP, PT, Tag)
        """
        # Format the speech text
        if isinstance(value, (int, float)):
            speech_text = f"{tag_type} {tag_name} value is {value}"
        else:
            speech_text = f"{tag_type} {tag_name} value is {str(value)}"
        
        self.speak(speech_text)
    
    def speak_search_results(self, found_tags, found_nodes):
        """
        Speak search results summary
        
        Args:
            found_tags (list): List of tags that were searched for
            found_nodes (list): List of nodes that were found
        """
        if not found_tags:
            self.speak("No VP, PT, or Tag patterns found in the transcription")
            return
        
        if not found_nodes:
            self.speak(f"No matching nodes found for the {len(found_tags)} tag(s) searched")
            return
        
        # Speak summary
        tag_count = len(found_tags)
        node_count = len(found_nodes)
        self.speak(f"Found {node_count} matching node(s) for {tag_count} tag(s)")
    
    def speak_error(self, error_message):
        """Speak error messages"""
        self.speak(f"Error: {error_message}")
    
    def speak_connection_status(self, connected, server_url):
        """Speak connection status"""
        if connected:
            self.speak(f"Connected to OPC-UA server at {server_url}")
        else:
            self.speak(f"Failed to connect to OPC-UA server at {server_url}")
    
    def stop(self):
        """Stop all speech and cleanup"""
        self.speech_queue.clear()
        self.is_speaking = False
        if self.engine:
            self.engine.stop()
    
    def set_voice_rate(self, rate):
        """Set speech rate"""
        self.engine.setProperty('rate', rate)
    
    def set_voice_volume(self, volume):
        """Set speech volume"""
        self.engine.setProperty('volume', volume)

# Global audio generator instance
audio_gen = AudioGenerator()

def speak_text(text, block=False):
    """Global function to speak text"""
    audio_gen.speak(text, block)

def speak_opcua_value(tag_name, value, tag_type="Tag"):
    """Global function to speak OPC-UA values"""
    audio_gen.speak_opcua_value(tag_name, value, tag_type)

def speak_search_results(found_tags, found_nodes):
    """Global function to speak search results"""
    audio_gen.speak_search_results(found_tags, found_nodes)

def speak_error(error_message):
    """Global function to speak errors"""
    audio_gen.speak_error(error_message)

def speak_connection_status(connected, server_url):
    """Global function to speak connection status"""
    audio_gen.speak_connection_status(connected, server_url) 